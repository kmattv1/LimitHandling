from src.dto.application import Application


class SetupCustomPublicApplicationLimits:
    def __init__(self, application_repository):
        self.application_repository = application_repository

    def set_custom_application_limits(self, application_name, exceptional_plan):
        if self.application_repository.contains(application_name):
            application = self.application_repository.get_application(application_name)

            if application.get_is_public():
                migration_application = Application(application.name, application.owner_organization, True, exceptional_plan)
                self.application_repository.add_application(migration_application)
                self.application_repository.remove_application(application)
