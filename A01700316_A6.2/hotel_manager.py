"""
Hotel Manager Module.

Classes and methods for managing hotels,
customers, and reservations.
"""

import json
import os
import sys


class Hotel:
    """Class representing a hotel."""

    def __init__(self, hotel_id, name, address, total_rooms):
        """Initialize a new Hotel instance."""
        self.hotel_id = hotel_id
        self.name = name
        self.address = address
        self.total_rooms = total_rooms

    def create_hotel(self, file_path):
        """Create a new hotel entry in the specified file."""
        hotels = self._load_data(file_path)
        hotels.append(self.__dict__)
        self._save_data(file_path, hotels)

    @staticmethod
    def _load_data(file_path):
        """Load data from a file."""
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []

    @staticmethod
    def _save_data(file_path, data):
        """Save data to a file."""
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)


class Customer:
    """Class representing a customer."""

    def __init__(self, customer_id, name, email):
        """Initialize a new Customer instance."""
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def create_customer(self, file_path):
        """Create a new customer entry in the specified file."""
        customers = Hotel._load_data(file_path)
        customers.append(self.__dict__)
        Hotel._save_data(file_path, customers)


class Reservation:
    """Class representing a reservation."""

    def __init__(self, reservation_id, hotel_id, customer_id):
        """Initialize a new Reservation instance."""
        self.reservation_id = reservation_id
        self.hotel_id = hotel_id
        self.customer_id = customer_id

    def create_reservation(self, file_path):
        """Create a new reservation entry in the specified file."""
        reservations = Hotel._load_data(file_path)
        reservations.append(self.__dict__)
        Hotel._save_data(file_path, reservations)


class HotelManager:
    """Class for managing hotels, customers, and reservations."""

    @staticmethod
    def process_file(file_path):
        """Process input from a file and perform corresponding actions."""
        if not os.path.exists(file_path):
            print(f"Error: The file {file_path} does not exist.")
            return

        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(';')
                if len(parts) < 2:
                    print(f"Invalid line format: {line}")
                    continue

                entity = parts[0].lower()
                if entity == 'hotel':
                    hotel = Hotel(parts[1], parts[2], parts[3], int(parts[4]))
                    hotel.create_hotel("hotels.json")
                elif entity == 'customer':
                    customer = Customer(parts[1], parts[2], parts[3])
                    customer.create_customer("customers.json")
                elif entity == 'reservation':
                    reservation = Reservation(parts[1], parts[2], parts[3])
                    reservation.create_reservation("reservations.json")
                else:
                    print(f"Unknown entity: {entity}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python hotel_manager.py <input_file.txt>")
    else:
        input_file = sys.argv[1]
        HotelManager.process_file(input_file)
