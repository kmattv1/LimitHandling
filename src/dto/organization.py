class Organization:
    def __init__(self,
                 name,
                 plan,
                 build_handler):
        self.name = name
        self.plan = plan
        self.build_handler = build_handler

    def get_name(self):
        return self.name

    def get_plan(self):
        return self.plan

    def get_build_handler(self):
        return self.build_handler