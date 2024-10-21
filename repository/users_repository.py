from repository.repository_interface import RepositoryInterface
from users.user import User


class UsersRepository(RepositoryInterface):

    def __init__(self):
        self.users = []

    def create(self, data):
        id = len(self.users) + 1
        user = User(user_id=id, **data)
        self.users.append(user)
        print(f"User {user.name} has been created")

    def read(self, entry_id):
        utilizator = None
        for user in self.users:
            if entry_id == user.user_id:
                utilizator = user
                break
        if utilizator:
            print(f"The Id is: {utilizator.user_id} \n"
                  f"Username is: {utilizator.name} \n"
                  f"User email is: {utilizator.email} \n"
                  #f"Parola utilizatorului: {utilizator.password}"
            )

        else:
            print(f"The user with id {entry_id} is not available.")

    def update(self, entry_id, new_data):
        utilizator = None
        for user in self.users:
            if entry_id == user.user_id:
                utilizator = user
                break
        if utilizator:
                user.name = new_data.get("name", utilizator.name)
                user.email = new_data.get("email", utilizator.email)
                #user.password = new_data.get("password", utilizator.password)
                print(f"User with the id: {utilizator.user_id} has been updated.")
        else:
            print(f"User with the id: {entry_id} hasn't been found.")

    def delete(self, entry_id):
        utilizator = None
        for user in self.users:
            if entry_id == user.user_id:
                utilizator = user
                break
        if utilizator:
            self.users.remove(utilizator)
            print(f"User with the id: {entry_id} has been deleted.")
        else:
            print(f"User with the id: {entry_id} hasn't been found.")
