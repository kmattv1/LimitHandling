from unittest import TestCase

from src.dto import plan
from src.dto.application import Application
from src.dto.organization import Organization
from src.repository.application_repository import ApplicationRepository
from src.repository.user_repository import UserRepository
from src.usecase.application.list_application_use_case import ListApplications


class TestListApplications(TestCase):

    def setUp(self):
        self.application_repository = ApplicationRepository()
        self.user_repository = UserRepository()
        free_plan = plan.Free()
        self.organization = Organization("test_org", free_plan, None)

    def test_given_repository_with_app_when_listing_applications_then_one_app_is_listed(self):
        # Given
        self.application_repository.add_application(Application("test_app", self.organization, False))
        assert len(self.application_repository.application_storage.keys()) is 1
        list_apps = ListApplications(self.application_repository)

        # When
        result = list_apps.get_app_names()

        # Then
        assert len(result) is 1
        assert list(result)[0] is "test_app"
