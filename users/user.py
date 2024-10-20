class User:

    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.__password = password


    def __validate_password(self):
        pass