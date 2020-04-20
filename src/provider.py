from dependency_injector import providers, containers

from src.repository.application_repository import ApplicationRepository
from src.repository.organization_repository import OrganizationRepository
from src.repository.plan_repository import PlanRepository
from src.repository.user_repository import UserRepository


class Repositories(containers.DeclarativeContainer):
    plan_repository = providers.Singleton(PlanRepository)
    organization_repository = providers.Singleton(OrganizationRepository)
    application_repository = providers.Singleton(ApplicationRepository)
    user_repository = providers.Singleton(UserRepository)
