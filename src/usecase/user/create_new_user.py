from src.dto.user import User
from src.usecase.http_messages import errors


class CreateNewUser:
    def __init__(self,
                 organization_repository,
                 user_repository):
        self.organization_repository = organization_repository
        self.user_repository = user_repository

    def create_new_user(self, user_name, email, organization_name):
        if self.organization_repository.contains(organization_name):
            organization = self.organization_repository.get_organization(organization_name)
            if not self.user_repository.contains(user_name):
                user = User(user_name, email, organization, False)
                return self.user_repository.add_user(user)
            else:
                raise errors.get_bad_request_error("There is a registered user with the same username!")
        else:
            raise errors.get_bad_request_error("Specified organization does not exits!")
