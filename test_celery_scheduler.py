"""
Tests for generic celery scheduler functionality
"""

from typing import cast
from unittest.mock import AsyncMock, MagicMock, NonCallableMagicMock, call, patch

import pytest
from celery import Task
from pytest_mock import MockerFixture

from common.models.enums import Vendors
from inventory_agent.celery_scheduler import (
    common_run_scheduler_by_vendor,
    common_scheduler_insert_into_buffer,
    enable_scheduled_tasks_by_vendor,
    start_scheduled_tasks_controller,
)
from inventory_agent.models.disable_initial_population import DisableInitialPopulation
from inventory_agent.redis.util import (
    ExecutingQueue,
    PendingQueue,
    celery_queue_length,
    get_disable_initial_population,
)
from inventory_agent.scheduled_population import (
    FORTIMANAGER_UPDATE_TASK,
    MERAKI_DELTA_UPDATE_TASK,
    MERAKI_FULL_UPDATE_TASK,
    MIST_UPDATE_TASK,
    RUN_SCHEDULER_ENTITY_TASK,
    VELOCLOUD_UPDATE_TASK,
    disable_run_entity_task_by_vendor,
    enable_run_entity_task_by_vendor,
    enable_scheduled_task,
)
from inventory_agent.settings import VENDORS
from tests.utils import target


@pytest.mark.xdist_group(name="inventory-agent-tests")
@pytest.mark.usefixtures("clear_redis")
class TestScheduledTasks:
    """
    Class for testing tasks and logic from the scheduler
    """

    def test_common_run_scheduler_by_vendor_execute_jobs(self, mocker):
        PendingQueue.add(name="foo", job_queue="BAR")
        mocker.patch(
            target(
                celery_queue_length,
                common_run_scheduler_by_vendor,
            ),
            return_value=1,
        )

        mocker.patch(
            target(
                disable_run_entity_task_by_vendor,
                common_run_scheduler_by_vendor,
            )
        )
        # Not working yet
        # mocker.patch("apply_async")
        # common_run_scheduler_by_vendor("BAR")

        # assert ExecutingQueue.exists() is True
        # executing = ExecutingQueue.get_first()
        # assert executing.name == "foo"
        # assert executing.job_queue == "bar"

    def test_common_scheduler_insert_false_into_buffer_false(self):
        """
        Tests if the items in the pending queues are not duplicated
        """
        PendingQueue.add(name="foo", job_queue="BAR")

        common_scheduler_insert_into_buffer("foo", "BARS")

        assert PendingQueue.get_first().job_queue == "BAR"
        assert PendingQueue.exists() is True
        assert PendingQueue.exists_by_vendor("BARS") is False
        assert PendingQueue.exists_by_vendor("BAR") is True
        assert len(PendingQueue.get_all()) == 1

    def test_common_scheduler_insert_into_buffer_true(self, mocker):
        """
        Tests if the items in the pending queues can have the same celery queue

        Args:
            mocker (_type_): _description_
        """
        PendingQueue.add(name="foo", job_queue="BAR")

        common_scheduler_insert_into_buffer("foos", "BARS")

        assert PendingQueue.exists() is True
        assert PendingQueue.exists_by_vendor("BAR") is True
        assert len(PendingQueue.get_all()) == 2
        assert PendingQueue.get_first().name == "foo"

    def test_common_run_scheduler_by_vendor_no_pending_jobs(self, mocker):
        """
        Test if there are no pending jobsfor the vendor, the task is not executed
        """

        mock_disable = mocker.patch(
            target(
                disable_run_entity_task_by_vendor,
                common_run_scheduler_by_vendor,
            )
        )
        mock_celery_queue_length = mocker.patch(
            target(
                celery_queue_length,
                common_run_scheduler_by_vendor,
            ),
            return_value=0,
        )

        common_run_scheduler_by_vendor("ANYTHING")

        assert ExecutingQueue.exists() is False
        assert mock_disable.not_called
        assert mock_celery_queue_length.called_once_with("BAR")
        assert mock_disable.not_called


@pytest.mark.xdist_group(name="inventory-agent-tests")
@pytest.mark.usefixtures("clear_redis")
@pytest.mark.parametrize("vendor", VENDORS)
def test_enable_scheduled_tasks_by_vendor(mocker: MockerFixture, vendor):
    """
    Test enabling the scheduled tasks for a specific vendor
    """
    enable_scheduled_task_mock: MagicMock | AsyncMock | NonCallableMagicMock = (
        mocker.patch(target(enable_scheduled_task, enable_scheduled_tasks_by_vendor))
    )

    enable_run_entity_task_by_vendor_mock: (
        MagicMock | AsyncMock | NonCallableMagicMock
    ) = mocker.patch(
        target(enable_run_entity_task_by_vendor, enable_scheduled_tasks_by_vendor)
    )

    enable_scheduled_tasks_by_vendor(vendor)

    match vendor:
        case "FORTIMANAGER":
            enable_scheduled_task_mock.assert_has_calls(
                [call(RUN_SCHEDULER_ENTITY_TASK), call(FORTIMANAGER_UPDATE_TASK)]
            )
            assert enable_scheduled_task_mock.call_count == 2
        case Vendors.VELOCLOUD:
            enable_scheduled_task_mock.assert_has_calls(
                [call(RUN_SCHEDULER_ENTITY_TASK), call(VELOCLOUD_UPDATE_TASK)]
            )
            assert enable_scheduled_task_mock.call_count == 2
        case Vendors.MERAKI:
            enable_scheduled_task_mock.assert_has_calls(
                [
                    call(RUN_SCHEDULER_ENTITY_TASK),
                    call(MERAKI_DELTA_UPDATE_TASK),
                    call(MERAKI_FULL_UPDATE_TASK),
                ]
            )
            assert enable_scheduled_task_mock.call_count == 3
        case Vendors.MIST:
            enable_scheduled_task_mock.assert_has_calls(
                [call(RUN_SCHEDULER_ENTITY_TASK), call(MIST_UPDATE_TASK)]
            )
            assert enable_scheduled_task_mock.call_count == 2

    enable_run_entity_task_by_vendor_mock.assert_called_once_with(vendor)
    assert enable_run_entity_task_by_vendor_mock.call_count == 1


@pytest.mark.xdist_group(name="inventory-agent-tests")
@pytest.mark.usefixtures("clear_redis")
@pytest.mark.parametrize("vendor", VENDORS)
@patch.object(start_scheduled_tasks_controller, "retry")
def test_start_scheduled_tasks_controller(mocker: MockerFixture, vendor):
    """
    Test the scheduler initial task controller
    """

    task = cast(Task, start_scheduled_tasks_controller)

    enable_scheduled_tasks_by_vendor_mock: (
        MagicMock | AsyncMock | NonCallableMagicMock
    ) = mocker.patch(
        target(enable_scheduled_tasks_by_vendor, start_scheduled_tasks_controller)
    )

    get_disable_initial_population_mock = mocker.patch(
        target(get_disable_initial_population, start_scheduled_tasks_controller)
    )

    task.apply()
    get_disable_initial_population_mock.assert_not_called()
    enable_scheduled_tasks_by_vendor_mock.assert_not_called()

    mocker.patch(
        target(get_disable_initial_population, start_scheduled_tasks_controller),
        return_value=None,
    )
    task.apply(kwargs={"vendor": vendor})
    enable_scheduled_tasks_by_vendor_mock.assert_not_called()

    mocker.patch(
        target(get_disable_initial_population, start_scheduled_tasks_controller),
        return_value=DisableInitialPopulation(),
    )
    enable_scheduled_tasks_by_vendor_mock.assert_not_called()

    mocker.patch(
        target(get_disable_initial_population, start_scheduled_tasks_controller),
        return_value=DisableInitialPopulation(
            meraki=True, velocloud=True, mist=True, fortimanager=True
        ),
    )
    enable_scheduled_tasks_by_vendor_mock.assert_called_once_with(vendor)
