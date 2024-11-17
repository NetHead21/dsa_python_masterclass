from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: float


class RawMaterial(Item):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price)
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"


class OfficeSupply(Item):
    def __init__(self, name: str, price: float, stock: int) -> None:
        super().__init__(name, price)
        self.stock = stock

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"


class ProcurementSystem:
    def __init__(self):
        self.items: list[Item] = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def display_items(self) -> None:
        print("Items in Procurement")
        for item in self.items:
            print(item)


item1 = RawMaterial("Steel", 999.99, 50)
item2 = OfficeSupply("Bond Paper", 999.99, 50)

procurement = ProcurementSystem()
procurement.add_item(item1)
procurement.add_item(item2)
procurement.display_items()
