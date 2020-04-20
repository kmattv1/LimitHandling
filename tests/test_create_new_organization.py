from unittest import TestCase

from src.repository.organization_repository import OrganizationRepository
from src.repository.plan_repository import PlanRepository
from src.repository.plans_enum import PlansEnum
from src.usecase.user.create_new_organization import CreateNewOrganization


class TestCreateNewOrganization(TestCase):
    def setUp(self):
        self.organization_repository = OrganizationRepository()
        self.plan_repository = PlanRepository()

    def test_given_empty_repository_when_creating_a_new_organization_then_repository_contains_new_org(self):
        # Given
        assert len(self.organization_repository.organization_storage.keys()) is 0
        create_new_organization_use_case = CreateNewOrganization(self.organization_repository, self.plan_repository)

        # When
        result = create_new_organization_use_case.create_new_organization("test_org", "pub")

        # Then
        assert result is True
        assert len(self.organization_repository.organization_storage.keys()) is 1
