# inventory: dict[str, int] = {}


# def check_item(item: str) -> bool:
#     return item in inventory


# def add_item(item: str, quantity: int) -> None:
#     inventory[item] = quantity
#     print(f"Added {inventory[item]}, {item}")


# def remove_item(item: str, quantity: int) -> None:
#     if check_item(item) and inventory[item] >= quantity:
#         inventory[item] -= quantity
#     else:
#         print(f"Not enough {item} in the inventory")


# def display_inventory() -> None:
#     print("\nCurrent Inventory")
#     for item, quantity in inventory.items():
#         print(f"Item: {item}, Quantity: {quantity}")


# # Adding items to the inventory
# add_item("Apples", 50)
# add_item("Bananas", 30)
# add_item("Oranges", 40)

# # Display Inventory
# display_inventory()

# # Removing items from the inventory
# remove_item("Apples", 20)
# remove_item("Bananas", 40)

# # Display Inventory
# display_inventory()
