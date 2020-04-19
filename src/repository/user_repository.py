class UserRepository:
    def __init__(self):
        self.user_storage = {}

    def get_user(self, user_name):
        return self.user_storage.get(user_name)

    def contains(self, user_name):
        return user_name in self.user_storage.keys()

    def add_user(self, user):
        user_name = user.get_name()
        user_object = {
            user_name: user
        }
        self.user_storage.update(user_object)
        return user_name in self.user_storage.keys()