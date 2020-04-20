from src.dto.organization import Organization


class OrganizationRepository:
    def __init__(self):
        self.organization_storage = {}

    def get_organization(self, organization_name):
        return self.organization_storage.get(organization_name)

    def contains(self, organization_name):
        return organization_name in self.organization_storage.keys()

    def add_organization(self, organization_name, plan, build_handler):
        organization = Organization(organization_name, plan, build_handler)
        organization_object = {
            organization_name: organization
        }
        self.organization_storage.update(organization_object)
        return organization_name in self.organization_storage.keys()

    def add_organization(self, organization):
        organization_name = organization.get_name()
        organization_object = {
            organization_name: organization
        }
        self.organization_storage.update(organization_object)
        return organization_name in self.organization_storage.keys()