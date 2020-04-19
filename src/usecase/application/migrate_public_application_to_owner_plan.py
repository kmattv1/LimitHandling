from src.dto.application import Application


class MigratePublicApplicationToOwnerPlan:
    def __init__(self, application_repository):
        self.application_repository = application_repository

    def migrate_from_public_to_private(self, application_name):
        if self.application_repository.contains(application_name):
            application = self.application_repository.get_application(application_name)

            self.application_repository.update_application_properties(application_name,
                                                                      application.owner_organization,
                                                                      False,
                                                                      None)
            return self.application_repository.get_application(application_name).get_is_public() is False
        return None
