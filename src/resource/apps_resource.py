import distutils.util
import json
from typing import Optional, Awaitable

import tornado.web

from src.usecase.application.list_application_use_case import ListApplications
from src.usecase.http_messages import errors
from src.usecase.load_json_to_tuple import parse_json_to_tuple
from src.usecase.user.create_new_app import CreateNewApplication


class AppsResource(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def initialize(self,
                   application_repository,
                   user_repository):
        self.application_repository = application_repository
        self.user_repository = user_repository

    def get(self):
        """
        Description end-point
        ---
        tags:
        - Example
        summary: List applications
        description: This resource will list plan based limits for the requested application.
        operationId: api.app
        produces:
        - application/json
        responses:
        "200":
          description: successful operation
        "404":
          description: failed operation
        "500":
          description: internal server error
        """

        list_apps_use_case = ListApplications(self.application_repository)
        self.write(json.dumps(list(list_apps_use_case.get_app_names())))

    def post(self):
        """
        Description end-point
        ---
        tags:
        - Example
        summary: Create a new application
        description: This resource will list plan based limits for the requested application.
        operationId: api.apps
        produces:
        - application/json
        parameters:
        - in: body
          name: appName
          description: Application name
          required: true
        - in: body
          name: isPublic
          description: Will set the application type based on this parameter name
          required: true
        responses:
        "200":
          description: successful operation
          schema:
            $ref: '#/definitions/Application'
        "400":
          description: bad request
        "404":
          description: failed operation
        "500":
          description: internal server error
        """
        try:
            body = parse_json_to_tuple(self.request.body.decode('utf-8'))
            app_name = str(body.appName)
            is_public = distutils.util.strtobool(body.isPublic)
            user_name = str(self.request.headers.get('user_name'))

            create_new_app_use_case = CreateNewApplication(self.application_repository, self.user_repository)
            self.write(create_new_app_use_case.create_application(app_name, is_public, user_name).get_as_dict())
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
