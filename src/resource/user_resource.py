from typing import Optional, Awaitable

import tornado.web

from src.usecase.http_messages import errors
from src.usecase.load_json_to_tuple import parse_json_to_tuple
from src.usecase.user.create_new_user import CreateNewUser


class UserResource(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def initialize(self,
                   organization_repository,
                   plan_repository):
        self.organization_repository = organization_repository
        self.plan_repository = plan_repository

    def post(self):
        """
        Description end-point
        ---
        tags:
        - Example
        summary: Create a new organization
        description: This resource will create a new organization.
        operationId: api.org
        produces:
        - application/json
        parameters:
        - in: body
          name: userName
          description: User name
          required: true
        - in: body
          name: email
          description: Email address
          required: true
        - in: body
          name: organizationName
          description: Name of the organization where the user is registered
          required: true
        responses:
        "200":
          description: successful operation
        "400":
          description: bad request
        "404":
          description: failed operation
        "500":
          description: internal server error
        """
        try:
            body = parse_json_to_tuple(self.request.body.decode('utf-8'))
            user_name = str(body.userName)
            email = str(body.email)
            organization_name = str(body.organizationName)

            create_new_user_use_case = CreateNewUser(self.organization_repository, self.plan_repository)
            user_created = create_new_user_use_case.create_new_user(user_name, email, organization_name)
            if user_created:
                self.write("Successfully created new user named: " + str(user_name))
            else:
                raise errors.get_internal_server_error("Failed to create new user")

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
