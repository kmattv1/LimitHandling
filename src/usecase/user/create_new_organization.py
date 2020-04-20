import logging

from src.dto.organization import Organization
from src.usecase.build_application.build_handler import BuildHandler
from src.usecase.http_messages import errors


class CreateNewOrganization:
    def __init__(self,
                 organization_repository,
                 plan_repository):
        self.organization_repository = organization_repository
        self.plan_repository = plan_repository

    def create_new_organization(self, organization_name, plan_name):
        if not self.organization_repository.contains(organization_name):
            plan_id = self.plan_repository.get_plan_id_for_name(plan_name)
            if self.plan_repository.contains(plan_id):
                try:
                    plan = self.plan_repository.get_plan(plan_id)
                    build_handler = BuildHandler(plan)
                    organization = Organization(organization_name, plan, build_handler)
                    return self.organization_repository.add_organization(organization)
                except Exception as e:
                    logging.error(e)
                    raise errors.get_internal_server_error("Failed to create organization due to server error!")
            else:
                raise errors.get_bad_request_error("There is no plan that matches with the specified one!")
        else:
            raise errors.get_bad_request_error("There is already an existing organization with this name!")
