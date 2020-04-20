from src.dto.application import Application


class ApplicationRepository:
    def __init__(self):
        self.application_storage = {}

    def get_applications(self):
        return self.application_storage.keys()

    def get_application(self, application_name):
        return self.application_storage.get(application_name)

    def contains(self, application_name):
        return application_name in self.application_storage.keys()

    def add_application(self, application):
        application_name = application.get_name()
        application_object = {
            application_name: application
        }
        self.application_storage.update(application_object)
        return self.application_storage.get(application_name)

    def remove_application(self, application_name):
        if application_name in self.application_storage.keys():
            del self.application_storage[application_name]

    def update_application_properties(self, application_name, organization, is_public, *exceptional_plan):
        if exceptional_plan:
            changed_application_definition = Application(application_name, organization, is_public, exceptional_plan[0])
        else:
            changed_application_definition = Application(application_name, organization, is_public)

        self.remove_application(application_name)
        self.add_application(changed_application_definition)
