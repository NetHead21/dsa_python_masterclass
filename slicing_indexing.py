municipality_cities_in_ncr = "Municipality of Pateros, Caloocan City, Marikina City, Makati City, Mandaluyong City, Muntinlupa City, City of Manila,  Navotas City, City of Malabon, Valenzuela City, Pasay City, Pasig City, Parañaque City, Quezon City, City of San Juan, Las Piñas City, Taguig City".split(
    ", "
)
print("List Operations:")
# Printing a list
print(f"Original List: {municipality_cities_in_ncr}")
# Slicing a list
print(f"Municipality in NCR: {municipality_cities_in_ncr[0]}")
# Slicing a list
print(f"Cities in NCR: {municipality_cities_in_ncr[1:]}")
# Slicing a list
print(f"Municipality or City in Even Indexes: {municipality_cities_in_ncr[::2]}")
# Reversing a list
print(f"List in reverse order: {municipality_cities_in_ncr[::-1]}")
print()

# Tuple Operation
print("\nTuple Operations:")
municipality_cities_in_ncr_tuple = tuple(municipality_cities_in_ncr)
print(f"Original Tuple: {municipality_cities_in_ncr_tuple}")
# Tuple slicing
print(
    f"Tuple slice from index 5 to last element: {municipality_cities_in_ncr_tuple[5:]}"
)
elements_in_odd_indexes = tuple(
    municipality_cities_in_ncr_tuple[i]
    for i in range(len(municipality_cities_in_ncr_tuple))
    if i % 2 != 0
)
print(f"Municipality or City in Odd Indexes: {elements_in_odd_indexes}")
# Reversing elements in a tuple
print(f"Reversed tuple: {municipality_cities_in_ncr_tuple[::-1]}")

# String operation
print("\nString Operations:")
my_string = "Juniven Saavedra/192.168.1.55/2024-11-13/18:00:00"
print(f"Original String: {my_string}")
# Slicing a string
print(f"Slicing a string: {my_string[:16]}")
# Splitting string into a list using '/' as the delimiter
my_string_to_list = my_string.split("/")
print(my_string_to_list)
# Every character in even indexes of the string
print(f"Characters in Even indexes of the string: {my_string[::2]}")
# Reversing a string
print(f"Reversing a string: {my_string[::-1]}")
