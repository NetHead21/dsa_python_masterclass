import dataclasses as dc


@dc.dataclass
class User:
    username: str
    password: str
    user_level: str


class Admin(User):
    def __init__(self, username: str, password: str, user_level: str) -> None:
        super().__init__(username, password, user_level)

    def display_info(self) -> str:
        return f"Admin Username: {self.username}, Admin Level {self.user_level}"


class LoginSystem:
    def __init__(self):
        self.users_data: dict[str, str] = {}

    def add_user(self, user: User) -> None:
        self.users_data[user.username] = user.password

    def verify_credentials(
        self, inputted_username: str, inputted_password: str
    ) -> bool:
        return (
            inputted_username in self.users_data
            and self.users_data[inputted_username] == inputted_password
        )

    @staticmethod
    def check_user_level(username: str) -> None:
        if "admin" in username:
            print("Hello, and Welcome Admin.")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if self.verify_credentials(username, password):
            print("Login successful!")
            self.check_user_level(username)
        else:
            print("Invalid username or password!")


def main():
    user1 = User("nethead21", "HelloWorld21", "normal")
    user2 = User("shalow", "Hello25", "normal")
    admin = Admin("admin", "admin", "admin")

    login_system = LoginSystem()
    login_system.add_user(user1)
    login_system.add_user(user2)
    login_system.add_user(admin)

    login_system.login()


if __name__ == "__main__":
    main()
