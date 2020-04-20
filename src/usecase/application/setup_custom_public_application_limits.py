from src.usecase.http_messages import errors


class SetupCustomPublicApplicationLimits:
    def __init__(self, application_repository):
        self.application_repository = application_repository

    def set_custom_application_limits(self, application_name, exceptional_plan):

        if self.application_repository.contains(application_name):
            application = self.application_repository.get_application(application_name)

            if application.get_is_public():
                self.application_repository.update_application_properties(application.get_name(),
                                                                          application.get_owner_organization(),
                                                                          True,
                                                                          exceptional_plan)
                return self.application_repository.get_application(application_name)
            else:
                raise errors.get_bad_request_error("Selected application is not a public application!")
        else:
            raise errors.get_not_found_error("Specified application: " + str(application_name) + " does not exist!")
