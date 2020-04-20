from unittest import TestCase

from src.dto import plan
from src.dto.application import Application
from src.dto.organization import Organization
from src.repository.application_repository import ApplicationRepository
from src.repository.user_repository import UserRepository
from src.usecase.application.list_limits_of_an_application import ListLimitsOfAnApplication


class TestListLimitsOfAnApplication(TestCase):

    def setUp(self):
        self.application_repository = ApplicationRepository()
        self.user_repository = UserRepository()
        free_plan = plan.Free()
        self.organization = Organization("test_org", free_plan, None)

    def test_given_repository_with_app_when_listing_application_limits_then_response_matches(self):
        # Given
        self.application_repository.add_application(Application("test_app", self.organization, False))
        assert len(self.application_repository.application_storage.keys()) is 1
        list_app_limits = ListLimitsOfAnApplication(self.application_repository)

        # When
        result = list_app_limits.get_limits("test_app")

        # Then
        assert result.get("ApplicationName") is "test_app"
        assert result.get("Plan") is "Free"
        assert result.get("IsPublic") is False
