import tornado.web
from tornado_swagger.setup import setup_swagger

from src import provider
from src.dto import plan
from src.dto.application import Application
from src.dto.organization import Organization
from src.dto.user import User
from src.resource.app_limit_resource import AppLimitResource
from src.resource.apps_resource import AppsResource
from src.resource.migration_resource import MigrationResource
from src.resource.organization_resource import OrganizationResource
from src.resource.root_resource import RootResource
from src.resource.user_resource import UserResource
from src.usecase.build_application.build_handler import BuildHandler


class WebApplication(tornado.web.Application):
    _routes = [
        tornado.web.url(r'/', RootResource),
        tornado.web.url(r'/api/apps', AppsResource, dict(
            application_repository=provider.Repositories.application_repository(),
            user_repository=provider.Repositories.user_repository())),
        tornado.web.url(r'/api/app/migrate/(.*)', MigrationResource, dict(
            application_repository=provider.Repositories.application_repository())),
        tornado.web.url(r'/api/app/limit/(.*)', AppLimitResource, dict(
            application_repository=provider.Repositories.application_repository(),
            user_repository=provider.Repositories.user_repository())),
        tornado.web.url(r'/api/org', OrganizationResource, dict(
            application_repository=provider.Repositories.organization_repository(),
            user_repository=provider.Repositories.plan_repository())),
        tornado.web.url(r'/api/user', UserResource, dict(
            application_repository=provider.Repositories.organization_repository(),
            user_repository=provider.Repositories.plan_repository())),
    ]

    @staticmethod
    def __add_test_data_to_repositories():
        test_plan = plan.Free()
        organization = Organization("testOrg", test_plan, BuildHandler(test_plan))
        user = User("testUser", "test@mail.com", organization, True)
        application = Application("testApp", organization, False)

        provider.Repositories.user_repository().add_user(user)
        provider.Repositories.organization_repository().add_organization(organization)
        provider.Repositories.application_repository().add_application(application)

    def __init__(self):
        settings = {
            'debug': True
        }

        self.__add_test_data_to_repositories()

        setup_swagger(self._routes,
                      swagger_url='/doc',
                      api_base_url='/',
                      description='Limit handling service based on subscription packages',
                      api_version='1.0.0',
                      title='LimitHandling API',
                      schemes=['http'],
                      )
        super(WebApplication, self).__init__(self._routes, **settings)
