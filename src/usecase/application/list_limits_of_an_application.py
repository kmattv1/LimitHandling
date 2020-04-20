from src.dto.application_limits import ApplicationLimits
from src.usecase.http_messages import errors


class ListLimitsOfAnApplication:
    def __init__(self, application_repository):
        self.application_repository = application_repository

    def get_limits(self, application_name):
        application = self.application_repository.get_application(application_name)
        if application:
            plan = application.get_plan()
            if plan:
                return ApplicationLimits.get_limits_dict(application, plan)
            else:
                raise errors.get_not_found_error("No plan defined for the selected application!")
        else:
            raise errors.get_not_found_error("Specified application: " + str(application_name) + " does not exist!")
