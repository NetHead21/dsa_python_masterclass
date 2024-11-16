from pprint import pprint

my_dict: dict[str, str | int] = {"name": "Juniven", "age": 30, "address": "Taguig City"}

pprint(my_dict)

my_dict["job"] = "Python Software Developer"

pprint(my_dict)

del my_dict["address"]

pprint(my_dict)
