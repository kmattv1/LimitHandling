from unittest import TestCase

from src.dto import plan
from src.dto.application import Application
from src.dto.organization import Organization
from src.dto.plan import Plan
from src.repository.application_repository import ApplicationRepository
from src.repository.user_repository import UserRepository
from src.usecase.application.setup_custom_public_application_limits import SetupCustomPublicApplicationLimits


class TestSetupCustomPublicApplicationLimits(TestCase):
    def setUp(self):
        self.application_repository = ApplicationRepository()
        self.user_repository = UserRepository()
        free_plan = plan.Free()
        self.organization = Organization("test_org", free_plan, None)

    def test_given_repository_with_public_app_when_setting_custom_plan_then_app_is_on_custom_plan(self):
        # Given
        self.application_repository.add_application(Application("test_app", self.organization, True))

        assert self.application_repository.application_storage.get("test_app").get_is_public() is True
        assert self.application_repository.application_storage.get("test_app").get_plan().get_name() is "Public"

        custom_app_plan_use_case = SetupCustomPublicApplicationLimits(self.application_repository)

        # When
        custom_plan = Plan("Custom", 10, 1000, 100, None, 1)
        result = custom_app_plan_use_case.set_custom_application_limits("test_app", custom_plan)

        # Then
        assert result.get_name() is "test_app"
        assert self.application_repository.application_storage.get("test_app").get_is_public() is True
        assert self.application_repository.application_storage.get("test_app").get_plan().get_name() is "Custom"
