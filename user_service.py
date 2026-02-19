class UserService:

    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.user_id] = user

    def find_user(self, user_id):
        return self.users.get(user_id, "User not found")

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
        else:
            return "User not found"

    def update_user(self, user_id, user_update):
        user = self.users.get(user_id)
        if user:
            if user_update.name:
                user.name = user_update.name
            if user_update.surname:
                user.surname = user_update.surname
            if user_update.email:
                user.email = user_update.email
            if user_update.password:
                user.password = user_update.password
            if user_update.birthday:
                user.birthday = user_update.birthday
        else:
            return "User not found"

    def get_number(self):
        return len(self.users)
