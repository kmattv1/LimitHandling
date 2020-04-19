from src.dto.plan import Public
from src.usecase.build_application.build_handler import BuildHandler


class Application:
    def __init__(self,
                 name,
                 owner_organization,
                 is_public,
                 *exceptional_plan):
        self.name = name
        self.owner_organization = owner_organization
        self.is_public = is_public

        if exceptional_plan:
            self.exceptional_plan = exceptional_plan[0]
            self.build_handler = BuildHandler(exceptional_plan[0])
        else:
            self.exceptional_plan = None
            self.build_handler = owner_organization.get_build_handler()

    def get_name(self):
        return self.name

    def get_owner_organization(self):
        return self.owner_organization

    def get_is_public(self):
        return self.is_public

    def get_plan(self):
        if self.is_public:
            if self.exceptional_plan:
                return self.exceptional_plan
            else:
                return Public()
        else:
            return self.owner_organization.get_plan()

    def get_build_handler(self):
        return self.build_handler
