from src.usecase.build_application.build_handler import BuildHandler


class CreateNewOrganization:
    def __init__(self,
                 organization_repository,
                 plan_repository):
        self.organization_repository = organization_repository
        self.plan_repository = plan_repository

    def create_new_organization(self, organization_name, plan_name):
        if not self.organization_repository.contains(organization_name):
            if self.plan_repository.contains(plan_name):
                plan = self.plan_repository.get_plan(plan_name)
                build_handler = BuildHandler(plan)
                self.organization_repository.add_organization(organization_name, plan, build_handler)
