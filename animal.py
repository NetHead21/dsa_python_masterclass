class Animal:
    def __init__(self, species: str) -> None:
        self.species = species

    def make_sound(self): ...


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meoaw!"


winnie_the_poohdle = Dog("Canine")
garfield = Cat("Feline")

print(f"Winnie the poohdle is member of {winnie_the_poohdle.species} species.")
print(f"Winnie the poohdle says {winnie_the_poohdle.make_sound()}")

print(f"Garfield is member of {garfield.species} species.")
print(f"Garfield says {garfield.make_sound()}")
