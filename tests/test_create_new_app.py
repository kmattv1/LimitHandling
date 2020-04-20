from unittest import TestCase

from src.dto.organization import Organization
from src.dto import plan
from src.dto.user import User
from src.repository.application_repository import ApplicationRepository
from src.repository.user_repository import UserRepository
from src.usecase.user.create_new_app import CreateNewApplication


class TestCreateNewApplication(TestCase):

    def setUp(self):
        self.application_repository = ApplicationRepository()
        self.user_repository = UserRepository()
        free_plan = plan.Free()
        organization = Organization("test_org", free_plan, None)
        self.user_repository.add_user(User("test_user", "test@user.com", organization, False))

    def test_given_empty_repository_when_creating_an_application_then_repository_contains_new_app(self):
        # Given
        assert len(self.application_repository.application_storage.keys()) is 0
        create_new_app_use_case = CreateNewApplication(self.application_repository, self.user_repository)

        # When
        result = create_new_app_use_case.create_application("test", False, "test_user")

        # Then
        assert result.name is "test"
        assert len(self.application_repository.application_storage.keys()) is 1
