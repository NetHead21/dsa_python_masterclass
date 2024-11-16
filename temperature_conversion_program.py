def celcius_to_fahrenheit(temperature: float) -> float:
    return (temperature * 9 / 5) + 32


def fahrenheit_to_celcius(temperature: float) -> float:
    return (temperature - 32) * 5 / 9


def celcius_to_kelvin(temperature: float) -> float:
    return temperature + 273.15


print("Select temperature conversion:")
print("1: Celsius to Fahrenheit")
print("2: Fahrenheit to Celsius")
print("3: Celsius to Kelvin")

choice = input("Enter choice (1/2/3): ")

match choice:
    case "1":
        temperature = float(input("Enter temperature in Celsius: "))
        fahrenheit = celcius_to_fahrenheit(temperature)
        print(f"{temperature} Celsius is equal to {fahrenheit:.2f} Fahrenheit")
    case "2":
        temperature = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celcius(temperature)
        print(f"{temperature} Fahrenheit is equal to {celsius:.2f} Celsius")
    case "3":
        temperature = float(input("Enter temperature in Kelvin: "))
        kelvin = celcius_to_kelvin(temperature)
        print(f"{temperature} Celsius is equal to {kelvin:.2f} Kelvin")
    case _:
        print("Invalid input. Please enter a valid choice (1/2/3) only.")
