import distutils.util
import json
from typing import Optional, Awaitable

import tornado.web

from src.dto.plan import Plan
from src.usecase.application.list_limits_of_an_application import ListLimitsOfAnApplication
from src.usecase.application.setup_custom_public_application_limits import SetupCustomPublicApplicationLimits
from src.usecase.http_messages import errors
from src.usecase.load_json_to_tuple import parse_json_to_tuple
from src.usecase.user.create_new_app import CreateNewApplication


class AppResource(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def initialize(self,
                   application_repository,
                   user_repository):
        self.application_repository = application_repository
        self.user_repository = user_repository

    def get(self, app_name):
        """
        Description end-point
        ---
        tags:
        - Example
        summary: List application limits
        description: This resource will list plan based limits for the requested application.
        operationId: api.app
        produces:
        - application/json
        parameters:
        - in: url
          name: app_name
          description: Application name
          required: true
        responses:
        "200":
          description: successful operation
          schema:
            $ref: '#/definitions/ApplicationLimits'
        "404":
          description: failed operation
        "500":
          description: internal server error
        """

        list_app_limits_use_case = ListLimitsOfAnApplication(self.application_repository)
        self.write(list_app_limits_use_case.get_limits(app_name))

    def put(self, app_name):
        """
        Description end-point
        ---
        tags:
        - Example
        summary: Update application plan
        description: This resource will change public application plan.
        operationId: api.app
        produces:
        - application/json
        parameters:
        - in: url
          name: app_name
          description: Application name
          required: true
        - in: body
          name: plan
          description: Application plan
          required: true
          schema:
            $ref: '#/definitions/Plan'
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
            body = parse_json_to_tuple(self.request.body.decode('utf-8'))
            setup_custom_application_limits = SetupCustomPublicApplicationLimits(self.application_repository)
            plan_tuple = body.plan
            exceptional_plan = Plan(str(plan_tuple.PlanName),
                                    int(plan_tuple.AllowedConcurrentBuilds),
                                    int(plan_tuple.BuildTimeLimitInMinutes),
                                    int(plan_tuple.MaximumBuildsPerMonth),
                                    int(plan_tuple.MaximumNumberOfTeamMembers),
                                    int(plan_tuple.MaximumNumberOfApps))
            updated_plan = setup_custom_application_limits.set_custom_application_limits(app_name,
                                                                                         exceptional_plan).get_as_dict()
            self.write(updated_plan)

        except ValueError:
            raise errors.get_bad_request_error("Request can not be parsed!")

    def post(self):
        """
        Description end-point
        ---
        tags:
        - Example
        summary: List application limits
        description: This resource will list plan based limits for the requested application.
        operationId: api.app
        produces:
        - application/json
        parameters:
        - in: url
          name: app_name
          description: Application name
          required: true
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
