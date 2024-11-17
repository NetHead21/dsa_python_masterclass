from dataclasses import dataclass
from datetime import date


@dataclass
class Reservation:
    guest_name: str
    reservation_date: date
    num_guests: int


class HotelReservation(Reservation):
    def __init__(
        self, guest_name: str, reservation_date: date, num_guests: int, room_type: str
    ) -> None:
        super().__init__(guest_name, reservation_date, num_guests)
        self.room_type = room_type


class RestaurantReservation(Reservation):
    def __init__(
        self,
        guest_name: str,
        reservation_date: date,
        num_guests: int,
        table_number: int,
    ) -> None:
        super().__init__(guest_name, reservation_date, num_guests)
        self.table_number = table_number


class ReservationSystem:
    def __init__(self):
        self.reservations: list[Reservation] = []

    def add_reservation(self, reservation: Reservation):
        self.reservations.append(reservation)

    def display_reservations(self):
        print("Reservations:")
        for reservation in self.reservations:
            print(reservation)


hotel_reservation = HotelReservation("John Doe", date(2024, 11, 25), 2, "Suite")
restaurant_reservation = RestaurantReservation("Alice Smith", date(2024, 11, 28), 4, 15)
reservation_system = ReservationSystem()
reservation_system.add_reservation(hotel_reservation)
reservation_system.add_reservation(restaurant_reservation)
reservation_system.display_reservations()
