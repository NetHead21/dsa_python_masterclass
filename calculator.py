def calculate(expression: str) -> int | None:
    try:
        return eval(expression)
    except ZeroDivisionError:
        print("Cannot Divide by Zero")
    except Exception:
        print("Invalid expression.")


again = True

while again:
    expression = input("Enter an expression: ")
    result = calculate(expression)

    if result is not None:
        print(f"Result: {result}")

    again = input("Do you want to calculate another expression? (yes/no): ")
    if again.lower() != "yes":
        again = False

print("Thank you!")
