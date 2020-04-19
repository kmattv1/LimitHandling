from unittest import TestCase

from src.dto import plan
from src.repository.organization_repository import OrganizationRepository
from src.repository.user_repository import UserRepository
from src.usecase.user.create_new_user import CreateNewUser


class TestCreateNewUser(TestCase):
    def setUp(self):
        self.organization_repository = OrganizationRepository()
        self.user_repository = UserRepository()
        self.organization_repository.add_organization("test_org", plan.Free, None)

    def test_given_empty_repository_when_creating_a_new_user_then_repository_contains_new_app(self):
        # Given
        assert len(self.user_repository.user_storage.keys()) is 0
        create_new_user_use_case = CreateNewUser(self.organization_repository, self.user_repository)

        # When
        result = create_new_user_use_case.create_new_user("test_user", "test@user.com", "test_org")

        # Then
        assert result is True
        assert len(self.user_repository.user_storage.keys()) is 1
