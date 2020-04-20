import logging

from src.usecase.http_messages import errors


class ListApplications:
    def __init__(self, application_repository):
        self.application_repository = application_repository

    def get_app_names(self):
        try:
            return self.application_repository.get_applications()
        except Exception as e:
            logging.error(e)
            raise errors.get_internal_server_error("Failed to list applications!")
