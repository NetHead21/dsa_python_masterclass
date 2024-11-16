def print_lines() -> None:
    print("=" * 25)


def save_date(file_name: str, data: tuple[str, ...]) -> None:
    try:
        with open(file_name, "a") as file:
            file.write(f"{data[0]}, {data[1]}\n")
    except Exception as error:
        print(f"Error while writing to file.")
        print(error)


def clean_data(data: str) -> list[str]:
    return data.replace("\n", "").split(", ")


def list_to_dict(data: list[str]) -> dict[str, str]:
    return {
        credential.split(", ")[0]: credential.split(", ")[1].strip()
        for credential in data
    }


def read_data(file_name: str) -> dict[str, str]:
    try:
        with open(file_name, "r") as file:
            return list_to_dict(file.readlines())
    except Exception as error:
        print(f"Error while reading file.")
        print(error)


def register() -> None:
    print()
    print_lines()
    print("Register new User")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    save_date("data.txt", (username, password))


def check_credentials(
    credentials: dict[str, str], username: str, password: str
) -> bool:
    return username in credentials and credentials[username] == password


def login(credentials: dict[str, str]) -> None:
    print()
    print("Login")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if check_credentials(credentials, username, password):
        print("Login successful")
    else:
        print("Invalid username or password. Please try again.")

def main() -> None:
    while True:
        print()
        print_lines()
        print("1: Register new User")
        print("2: Login")
        print("3: Exit")

        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                register()
            case 2:
                saved_credentials = read_data("data.txt")
                login(saved_credentials)
            case 3:
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    print("Thank You!")
