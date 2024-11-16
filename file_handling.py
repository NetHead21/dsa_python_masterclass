def save_student_details(first_name: str, last_name: str) -> None:
    try:
        with open("student_details.txt", "a") as file:
            file.write(f"First Name: {first_name}, Last Name: {last_name}\n")
    except FileNotFoundError:
        print("File Not Found!")


while True:
    first_name = input("Enter the student's first name: ")
    last_name = input("Enter the student's last name: ")

    save_student_details(first_name=first_name, last_name=last_name)

    choice = input("Do you want to add another student? (yes/no): ").lower()
    if choice != "yes":
        print(f"Student First Name: {first_name}, Last Name: {last_name} saved.")
        break
