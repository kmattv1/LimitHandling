from unittest import TestCase
from unittest.mock import MagicMock

from src.dto.plan import Plan
from src.usecase.build_application.build import Build
from src.usecase.build_application.build_handler import BuildHandler
from src.usecase.build_application.build_status import BuildStatus


class TestBuildHandler(TestCase):

    def test_given_mock_plan_with_maximum_two_build_in_month_when_third_build_scheduled_then_limit_exceeded_error(self):
        # Given
        mock_plan = Plan("test", 1, 1, 2, 1, 1)
        build_handler = BuildHandler(mock_plan)
        mock_build = Build("test")
        mock_build.run = MagicMock(return_value=mock_instant_build())

        #  When
        build_handler.add_build_to_the_job_queue(mock_build)
        build_handler.add_build_to_the_job_queue(mock_build)
        status = build_handler.add_build_to_the_job_queue(mock_build)

        # Then
        assert status == BuildStatus.FAILED_WITH_MONTHLY_LIMIT_EXCEEDED

    def test_given_mock_plan_with_maximum_two_build_in_month_when_first_build_scheduled_then_success(self):
        # Given
        mock_plan = Plan("test", 1, 1, 2, 1, 1)
        build_handler = BuildHandler(mock_plan)
        mock_build = Build("test")
        mock_build.run = MagicMock(return_value=mock_instant_build())

        #  When
        status = build_handler.add_build_to_the_job_queue(mock_build)

        # Then
        assert status == BuildStatus.SUCCESSFUL


async def mock_instant_build():
    return BuildStatus.SUCCESSFUL
