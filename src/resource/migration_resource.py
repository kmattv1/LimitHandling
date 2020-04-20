from typing import Optional, Awaitable

import tornado.web

from src.usecase.application.migrate_public_application_to_owner_plan import MigratePublicApplicationToOwnerPlan
from src.usecase.http_messages import errors


class MigrationResource(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def initialize(self,
                   application_repository):
        self.application_repository = application_repository

    def put(self, app_name):
        """
        Description end-point
        ---
        tags:
        - Example
        summary: Migrate public application to private plan
        description: This resource will migrate public application to owners plan.
        operationId: api.migrate
        produces:
        - application/json
        parameters:
        - in: url
          name: app_name
          description: Application name
          required: true
        responses:
        "204":
          description: successful operation
        "400":
          description: bad request
        "404":
          description: failed operation
        "500":
          description: internal server error
        """

        try:
            migrate_application_use_case = MigratePublicApplicationToOwnerPlan(self.application_repository)
            migrated = migrate_application_use_case.migrate_from_public_to_private(app_name)

            if migrated:
                self.write("Successfully migrated " + str(app_name) + " to a private app")
            else:
                raise errors.get_internal_server_error("Migration failed")

        except ValueError:
            raise errors.get_bad_request_error("Request can not be parsed!")

    def write_error(self, *args, **kwargs):
        err_cls, err, traceback = kwargs['exc_info']
        if err:
            if err.status_code:
                self.set_status(err.status_code)
            if err.log_message:
                self.write(err.log_message)
        self.finish()
