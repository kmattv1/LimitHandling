class User:
    def __init__(self,
                 name,
                 email,
                 organization,
                 is_admin):
        self.name = name
        self.email = email
        self.organization = organization
        self.is_admin = is_admin

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_organization(self):
        return self.organization

    def get_is_admin(self):
        return self.is_admin
