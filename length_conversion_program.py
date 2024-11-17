menu_str = """
Select conversion:
1. Feet to Inches
2. Inches to Feet
3. Feet to Meters
4. Meters to Feet
5. Meters to Inches
6. Inches to Meters
"""


def get_user_input(label: str, required: bool = True) -> str:
    value = input(f"{label}: ") or None
    while required and not value:
        value = input(f"{label}: ")
    return value


def convert(option: int, measurement: float) -> None:
    conversion: dict[int, str] = {
        1: f"{measurement} is equal to {round(measurement * 12, 2)} in inches.",
        2: f"{measurement} is equal to {round(measurement / 12, 2)} in feet.",
        3: f"{measurement} is equal to {round(measurement * 0.3048, 2)} in meters.",
        4: f"{measurement} is equal to {round(measurement / 0.3048, 2)} in feet.",
        5: f"{measurement} is equal to {round(measurement * 39.3701, 2)} in inches.",
        6: f"{measurement} is equal to {round(measurement * 0.0254, 2)} in meters",
    }

    print(conversion[option])


print(menu_str)

choice = int(get_user_input("Enter choice (1/2/3/4/5/6): "))
measurement = float(get_user_input("Enter measurement: "))

convert(choice, measurement)
