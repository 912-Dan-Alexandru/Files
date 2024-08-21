"""
Celery Scheduler Main
"""

from typing import cast

from celery import Celery, Task, current_app, shared_task
from celery.result import AsyncResult

from common.tools import TMFLogger

from .messages import CelerySchedulerMessages as Messages
from .models import TaskStatus
from .redis.util import (
    ExecutedQueue,
    ExecutingQueue,
    PendingQueue,
    celery_queue_length,
    get_disable_initial_population,
)
from .scheduled_population import (
    CHECK_SCHEDULER_ENTITY_TASK,
    FORTIMANAGER_UPDATE_TASK,
    INITIAL_SCHEDULER_CONTROLLER_TASK,
    INSERT_INTO_BUFFER_TASK,
    MERAKI_DELTA_UPDATE_TASK,
    MERAKI_FULL_UPDATE_TASK,
    MIST_UPDATE_TASK,
    RUN_SCHEDULER_ENTITY_TASK,
    VELOCLOUD_UPDATE_TASK,
    disable_scheduled_task,
    enable_scheduled_task,
)
from .settings import get_config

DEFAULT_THRESHOLD = 5
logger = TMFLogger()


def enable_scheduled_tasks():
    """Method to enable all the scheduled tasks"""
    enable_scheduled_task(RUN_SCHEDULER_ENTITY_TASK)
    enable_scheduled_task(CHECK_SCHEDULER_ENTITY_TASK)
    if get_config().get_bool("velocloud", "populate"):
        enable_scheduled_task(VELOCLOUD_UPDATE_TASK)
    if get_config().get_bool("meraki", "populate"):
        enable_scheduled_task(MERAKI_DELTA_UPDATE_TASK)
        enable_scheduled_task(MERAKI_FULL_UPDATE_TASK)
    if get_config().get_bool("mist", "populate"):
        enable_scheduled_task(MIST_UPDATE_TASK)
    if get_config().get_bool("fortimanager", "populate"):
        enable_scheduled_task(FORTIMANAGER_UPDATE_TASK)


@shared_task(
    name=INITIAL_SCHEDULER_CONTROLLER_TASK,
    bind=True,
    max_retries=None,
    default_retry_delay=30,
)
def start_scheduled_tasks_controller(self: Task):
    """
    Task to add the scheduled tasks once the initial population has finished.
    It removes itself from the scheduler queue once it runs.
    """
    initial_population_finished = get_disable_initial_population()
    celery_queue_len = celery_queue_length()
    if initial_population_finished and celery_queue_len < DEFAULT_THRESHOLD:
        logger.log(
            Messages.START_SCHEDULING_UPDATE_TASKS,
            queue_length=celery_queue_len,
            queue_max=DEFAULT_THRESHOLD,
        )
        enable_scheduled_tasks()
    elif initial_population_finished:
        logger.log(
            Messages.START_SCHEDULING_UPDATE_TASKS_FAILED,
            queue_length=celery_queue_len,
            queue_max=DEFAULT_THRESHOLD,
        )
        self.retry(exc="Initial Population is still in progress")
    else:
        logger.log(
            Messages.START_SCHEDULING_INITIAL_POPULATION_INCOMPLETE,
            initial_population=initial_population_finished,
        )
        self.retry(exc="Initial Population is still in progress")


@shared_task(name=INSERT_INTO_BUFFER_TASK)
def common_scheduler_insert_into_buffer(name: str):
    """
    Celery task that inserts into redis pending list (key: inventory-agent:pending-jobs)
    a task.
    """
    pending_items = [item.name for item in PendingQueue.get_all()]
    if name not in pending_items:
        PendingQueue.add(name=name)
    else:
        logger.log(
            Messages.SKIP_SCHEDULED_TASK,
            task_name=name,
            pending_items=len(pending_items),
        )


@shared_task(name=RUN_SCHEDULER_ENTITY_TASK)
def common_run_scheduler_entity():
    """
    Celery task that starts execution of the last task from pending list
    (key: inventory-agent:pending-jobs)
    """
    if PendingQueue.exists() and celery_queue_length() < DEFAULT_THRESHOLD:
        try:
            disable_scheduled_task(RUN_SCHEDULER_ENTITY_TASK)
        except KeyError:
            logger.log(
                Messages.SCHEDULER_ENTRY_VALUE_ERROR,
                redis_key="redbeat:" + RUN_SCHEDULER_ENTITY_TASK,
            )
            return

        next_job = PendingQueue.remove_first()
        scheduled_task: Task = cast(Celery, current_app).signature(next_job.name)
        res: AsyncResult = scheduled_task.apply_async()
        job_id = str(res.id)
        ExecutingQueue.add(next_job, job_id)
        logger.log(
            Messages.JOB_EXECUTION_STARTED,
            task_name=next_job.name,
            task_id=job_id,
            scheduled_time=next_job.jobRecieveDate,
        )


@shared_task(name=CHECK_SCHEDULER_ENTITY_TASK)
def common_check_scheduler_entity():
    """
    Celery task that checks for inventory-agent task unlock failures.
    If the celery queue is empty, it will remove the task from the pending items
    and re-enable the run_scheduler_entity task.
    """
    if ExecutingQueue.exists() and celery_queue_length() < DEFAULT_THRESHOLD:
        task = ExecutingQueue.remove_first()
        TMFLogger().log(
            Messages.JOB_FAILURE_UNTERMINATED,
            name=task.name,
            start_date=task.jobStartDate,
        )
        ExecutedQueue.add(task, TaskStatus.EXECUTING)
        enable_scheduled_task(RUN_SCHEDULER_ENTITY_TASK)
