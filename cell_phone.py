class SimCard:
    def __init__(self, phone_number: str, carrier: str) -> None:
        self.phone_number = phone_number
        self.carrier = carrier
        self.is_active: bool = False

    def activate(self) -> None:
        self.is_active = True
        print(f"Sim card activated for {self.phone_number} with {self.carrier}")

    def deactivate(self) -> None:
        self.is_active = False
        print(f"Sim card deactivated for {self.phone_number}")


class CellPhone:
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model
        self.sim_card = None

    def init_sim_card(self, sim_card: SimCard) -> None:
        if self.sim_card is None:
            self.sim_card = sim_card
            print(
                f"Inserted {sim_card.carrier} SIM card into {self.brand} {self.model}."
            )
        else:
            print("There is already a SIM card inserted.")

    def remove_sim_card(self) -> None:
        if self.sim_card is not None:
            removed_sim = self.sim_card
            self.sim_card = None
            print(
                f"Removed {removed_sim.carrier} SIM card from {self.brand} {self.model}."
            )
        else:
            print("There is no SIM card inserted.")

    def make_call(self, number: str) -> None:
        if self.sim_card is not None and self.sim_card.is_active:
            print(f"Making a call from {self.sim_card.phone_number} to {number}")
        else:
            print("Cannot make a call. Please insert a active SIM card.")


sim_card = SimCard("09408330570", "Globe")
phone = CellPhone("iPhone", "16 Pro Max")

phone.init_sim_card(sim_card)
phone.make_call("09408330523")

sim_card.activate()
phone.make_call("09408330523")

phone.remove_sim_card()
