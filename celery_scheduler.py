"""
Celery Scheduler Main
"""

from typing import cast

from celery import Celery, Task, current_app, shared_task
from celery.result import AsyncResult

from common.models.enums import Vendors
from common.tools import TMFLogger
from inventory_agent.models.disable_initial_population import DisableInitialPopulation

from .messages import CelerySchedulerMessages as Messages
from .models import TaskStatus
from .redis.util import (
    ExecutedQueue,
    ExecutingQueue,
    PendingQueue,
    celery_queue_length,
    get_disable_initial_population,
    set_disable_initial_population,
)
from .scheduled_population import (
    CHECK_SCHEDULER_ENTITY_TASK,
    FORTIMANAGER_UPDATE_TASK,
    INITIAL_POPULATION_TASK,
    INITIAL_SCHEDULER_CONTROLLER_TASK,
    INSERT_INTO_BUFFER_TASK,
    MERAKI_DELTA_UPDATE_TASK,
    MERAKI_FULL_UPDATE_TASK,
    MIST_UPDATE_TASK,
    RUN_SCHEDULER_ENTITY_TASK,
    UPDATE_SCHEDULER_ENTITY_TASK,
    VELOCLOUD_UPDATE_TASK,
    disable_run_entity_task_by_vendor,
    enable_run_entity_task_by_vendor,
    enable_scheduled_task,
)
from .settings import get_enabled_vendors

DEFAULT_THRESHOLD = 5
logger = TMFLogger()


def enable_scheduled_tasks_by_vendor(vendor: str) -> None:
    """
    Controller for enabling the correct task for a specific vendor
    """
    enable_scheduled_task(RUN_SCHEDULER_ENTITY_TASK)
    enable_run_entity_task_by_vendor(vendor)
    match vendor:
        case "FORTIMANAGER":
            enable_scheduled_task(FORTIMANAGER_UPDATE_TASK)
        case Vendors.VELOCLOUD:
            enable_scheduled_task(VELOCLOUD_UPDATE_TASK)
        case Vendors.MERAKI:
            enable_scheduled_task(MERAKI_DELTA_UPDATE_TASK)
            enable_scheduled_task(MERAKI_FULL_UPDATE_TASK)
        case Vendors.MIST:
            enable_scheduled_task(MIST_UPDATE_TASK)


def common_run_scheduler_by_vendor(vendor: str) -> None:
    """
    Sends the specific tasks for each vendor on their queue
    It checks if there are vendor tasks on the pending queue
    and disables other tasks for that vendor
    """
    if (
        PendingQueue.exists()
        and PendingQueue.exists_by_vendor(vendor)
        and celery_queue_length(vendor) < DEFAULT_THRESHOLD
    ):
        try:
            disable_run_entity_task_by_vendor(vendor)
        except KeyError:
            logger.log(
                Messages.SCHEDULER_ENTRY_VALUE_ERROR,
                redis_key="redbeat:" + RUN_SCHEDULER_ENTITY_TASK,
            )
            return

        next_job = PendingQueue.remove_first_by_vendor(vendor)
        if next_job is None:
            return
        scheduled_task: Task = cast(Celery, current_app).signature(next_job.name)
        res: AsyncResult = scheduled_task.apply_async(queue=vendor)
        job_id = str(res.id)
        ExecutingQueue.add(next_job, job_id)
        logger.log(
            Messages.JOB_EXECUTION_STARTED,
            task_name=next_job.name,
            task_queue=next_job.job_queue,
            task_id=job_id,
            scheduled_time=next_job.jobReceiveDate,
        )


@shared_task(
    name=INITIAL_SCHEDULER_CONTROLLER_TASK,
    bind=True,
    max_retries=None,
    default_retry_delay=30,
)
def start_scheduled_tasks_controller(self: Task, vendor=None) -> None:
    """
    Task to add the scheduled tasks once the initial population has finished
    for each vendor. It removes itself from the scheduler queue once it runs.
    """
    if vendor is None:
        return
    initial_population_finished = get_disable_initial_population()
    if (
        initial_population_finished is not None
        and initial_population_finished.get_vendor(vendor)
    ):
        logger.log(Messages.START_SCHEDULING_UPDATE_TASKS, vendor=vendor)
        enable_scheduled_tasks_by_vendor(vendor)
    else:
        logger.log(
            Messages.START_SCHEDULING_INITIAL_POPULATION_INCOMPLETE,
            vendor=vendor,
        )
        self.retry(exc=f"Initial Population for {vendor} is still in progress")


@shared_task(name=INSERT_INTO_BUFFER_TASK)
def common_scheduler_insert_into_buffer(name: str, queue: str) -> None:
    """
    Celery task that inserts into redis pending list (key: inventory-agent:pending-jobs)
    a task.
    """
    pending_items = [item.name for item in PendingQueue.get_all()]
    if name not in pending_items:
        PendingQueue.add(name=name, job_queue=queue)
    else:
        logger.log(
            Messages.SKIP_SCHEDULED_TASK,
            task_name=name,
            pending_items=len(pending_items),
        )


@shared_task(name=RUN_SCHEDULER_ENTITY_TASK)
def common_run_scheduler_entity(vendor_queue_ready: dict[str, bool]) -> None:
    """
    Celery task that starts execution of the last task from pending list for each vendor
    if the task is enabled for that vendor.
    (key: inventory-agent:pending-jobs)
    """
    for vendor in get_enabled_vendors():
        if vendor_queue_ready.get(vendor, False):
            common_run_scheduler_by_vendor(vendor)


@shared_task(name=CHECK_SCHEDULER_ENTITY_TASK)
def common_check_scheduler_entity() -> None:
    """
    Celery task that checks for inventory-agent task unlock failures.
    If the celery queue is empty, it will remove the task from the executing queue
    and re-enable the run_scheduler_entity task.

    It is slightly deprecated. Needs to be updated as soon as possible
    """

    if ExecutingQueue.exists():
        task = ExecutingQueue.get_first()
        if celery_queue_length(task.job_queue) < DEFAULT_THRESHOLD:
            ExecutingQueue.remove_first()
            TMFLogger().log(
                Messages.JOB_FAILURE_UNTERMINATED,
                name=task.name,
                queue=task.job_queue,
                start_date=task.jobStartDate,
            )
            ExecutedQueue.add(task, TaskStatus.IDLE)
            enable_scheduled_task(RUN_SCHEDULER_ENTITY_TASK)


@shared_task(name=UPDATE_SCHEDULER_ENTITY_TASK)
def update_scheduler_entity_status(task_status: TaskStatus, vendor: str):
    """
    Celery task that update task status to `COMPLETED` or `FAILED`
    Mark Scheduler Entity as complete and continue
    """
    TMFLogger().log(Messages.SCHEDULED_POPULATION_COMPLETE, vendor=vendor)
    if ExecutingQueue.exists():
        current_job = ExecutingQueue.remove_first_by_vendor(vendor.upper())
        if current_job:
            ExecutedQueue.add(current_job, task_status)
        enable_run_entity_task_by_vendor(vendor.upper())


@shared_task(name=INITIAL_POPULATION_TASK)
def initial_population_controller(disable_initial_population: DisableInitialPopulation):
    """
    Celery task to update redis key `inventory-agent:disable-initial-population` when a
    vendor finishes the initial population.
    """
    TMFLogger().log(
        Messages.INITIAL_POPULATION_COMPLETE,
        vendor=list(disable_initial_population.dict(exclude_unset=True).keys()),
    )
    if (redis_initial_population := get_disable_initial_population()) is not None:
        set_disable_initial_population(
            redis_initial_population | disable_initial_population
        )
