# RailwayReservationSystem.py
# Main runner file for Railway Reservation System project

from RailwayReservationSystemBackend import RailwaySystem
import input

def main():
    # Create Railway System instance
    system = RailwaySystem()

    # Collect user inputs
    passenger_name, train_number = input.get_inputs()

    # Try booking a ticket
    confirmation = system.book_ticket(passenger_name, train_number)
    print(confirmation)

if __name__ == "__main__":
    main()
