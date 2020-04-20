from src.dto import plan
from src.repository.plans_enum import PlansEnum


class PlanRepository:
    def __init__(self):
        self.plan_storage = {}

        default_plans = {
            PlansEnum.FREE: plan.Free,
            PlansEnum.DEV: plan.Developer,
            PlansEnum.ORG: plan.Organization,
            PlansEnum.PUB: plan.Public
        }

        self.plan_storage.update(default_plans)

    def contains(self, plan_id):
        return plan_id in self.plan_storage.keys()

    def get_plan(self, plan_id):
        return self.plan_storage.get(plan_id)

    @staticmethod
    def get_plan_id_for_name(plan_name):
        if "free" == str(plan_name).lower():
            return PlansEnum.FREE
        if "dev" == str(plan_name).lower():
            return PlansEnum.DEV
        if "org" == str(plan_name).lower():
            return PlansEnum.ORG
        if "pub" == str(plan_name).lower():
            return PlansEnum.PUB
        return None
