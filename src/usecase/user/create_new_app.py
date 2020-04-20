from src.dto.application import Application
from src.usecase.http_messages import errors


class CreateNewApplication:
    def __init__(self,
                 application_repository,
                 user_repository):
        self.application_repository = application_repository
        self.user_repository = user_repository

    def create_application(self, application_name, is_public, user_name):
        user = self.user_repository.get_user(user_name)

        if user:
            if not self.application_repository.contains(application_name):
                application = Application(application_name, user.get_organization(), is_public)
                return self.application_repository.add_application(application)
            else:
                raise errors.get_bad_request_error("There is already an existing application with this name!")
        else:
            raise errors.get_not_found_error("There is no registered user by the name: " + str(user_name))

