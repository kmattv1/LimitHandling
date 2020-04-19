from unittest import TestCase

from src.dto import plan
from src.dto.application import Application
from src.dto.organization import Organization
from src.repository.application_repository import ApplicationRepository
from src.repository.user_repository import UserRepository
from src.usecase.application.migrate_public_application_to_owner_plan import MigratePublicApplicationToOwnerPlan


class TestMigratePublicApplicationToOwnerPlan(TestCase):
    def setUp(self):
        self.application_repository = ApplicationRepository()
        self.user_repository = UserRepository()
        free_plan = plan.Free()
        self.organization = Organization("test_org", free_plan, None)

    def test_given_repository_with_public_app_when_migrating_application_then_app_is_on_free_plan(self):
        # Given
        self.application_repository.add_application(Application("test_app", self.organization, True))

        assert self.application_repository.application_storage.get("test_app").get_is_public() is True
        assert self.application_repository.application_storage.get("test_app").get_plan().get_name() is "Public"

        migrate_public_app_use_case = MigratePublicApplicationToOwnerPlan(self.application_repository)

        # When
        result = migrate_public_app_use_case.migrate_from_public_to_private("test_app")

        # Then
        assert result is True
        assert self.application_repository.application_storage.get("test_app").get_is_public() is False
        assert self.application_repository.application_storage.get("test_app").get_plan().get_name() is "Free"
