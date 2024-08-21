"""
Celery Scheduler Main Initialization
"""
import sys

from celery import Celery, signals
from celery.app.task import Task
from celery.exceptions import CeleryError
from structlog import get_logger

from common.config.celery_config import CeleryConfig
from common.database.redis import RedisDB
from common.tools.tmf_logger import TMFLogger

from .base_tasks import BaseTaskWithRetry
from .messages import WorkerAppMessages as Messages
from .scheduled_population import (
    INITIAL_SCHEDULER_CONTROLLER_TASK,
    setup_scheduled_population,
)
from .settings import get_celery_settings


@signals.worker_ready.connect
def start_scheduled_population(sender: Task, **_):
    """Start Scheduled population when the worker starts"""
    sender.app.send_task(INITIAL_SCHEDULER_CONTROLLER_TASK, queue="SchedulerController")


def main() -> Celery:
    """This main will initialise the celery_scheduler_app"""
    celery_config = get_celery_settings()
    RedisDB(uri=celery_config.backend).connect()
    RedisDB(uri=celery_config.broker).connect()

    try:
        celery_app = CeleryConfig.set_celery("inventory_agent", celery_config)
        celery_app.task_cls = BaseTaskWithRetry
        celery_app.conf["imports"] = [
            "inventory_agent.celery_scheduler",
            "inventory_agent.celery_signals",
        ]
        celery_app.conf["beat_scheduler"] = "redbeat.schedulers.RedBeatScheduler"
        setup_scheduled_population()
        return celery_app
    except (AttributeError, CeleryError, ValueError):
        logger = TMFLogger(get_logger("inventory_agent"))
        logger.log(Messages.CREATE_CELERY_APPLICATION_FAILED, exc_info=True)
        sys.exit()


celery = main()
