# RailwayReservationSystemBackend.py
# Backend logic for Railway Reservation System

class RailwaySystem:
    def __init__(self):
        # Predefined train data
        self.trains = {
            "101": {"name": "Express A", "seats": 2},
            "202": {"name": "Express B", "seats": 3}
        }

    def book_ticket(self, passenger_name: str, train_number: str) -> str:
        """
        Books a ticket if seats are available
        :param passenger_name: name of passenger
        :param train_number: train number to book
        :return: confirmation message
        """
        if train_number not in self.trains:
            return "Invalid train number."

        train = self.trains[train_number]
        if train["seats"] > 0:
            train["seats"] -= 1
            return f"Ticket confirmed for {passenger_name} on {train['name']}."
        else:
            return "Sorry, no seats available."
