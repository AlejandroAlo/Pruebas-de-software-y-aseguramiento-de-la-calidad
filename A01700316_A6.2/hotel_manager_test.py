"""
Unit tests for HotelManager module.
"""

import unittest
import os
import json
from hotel_manager import HotelManager


class TestHotelManager(unittest.TestCase):
    """Test case for HotelManager functionalities."""

    def setUp(self):
        """Set up test environment by cleaning existing files."""
        self.hotel_file = "hotels.json"
        self.customer_file = "customers.json"
        self.reservation_file = "reservations.json"
        self.cleanup()

    def tearDown(self):
        """Clean up test environment after each test."""
        self.cleanup()

    def cleanup(self):
        """Remove temporary files created during tests."""
        for file in [self.hotel_file, self.customer_file, self.reservation_file]:
            if os.path.exists(file):
                os.remove(file)

    def test_process_file(self):
        """
        Test the process_file method.

        This test checks if the input file is processed correctly and
        verifies that the corresponding data is stored in the appropriate files.
        """
        input_file = "test_input.txt"

        # Create a temporary test input file
        with open(input_file, 'w', encoding='utf-8') as file:
            file.write(
                "Hotel;H001;Hotel Safi Inn;Lazaro 109;50\n"
                "Hotel;H002;Parras Hotel;Ave Revolucion 54;100\n"
                "Customer;C001;Manuel Palacios;manuel@example.com\n"
                "Customer;C002;Pablo Landeros;pablol@example.com\n"
                "Reservation;R001;H001;C001\n"
                "Reservation;R002;H002;C002\n"
            )

        # Process the test input file
        HotelManager.process_file(input_file)

        # Verify hotels were created
        with open(self.hotel_file, 'r', encoding='utf-8') as file:
            hotels = json.load(file)
            self.assertEqual(len(hotels), 2)
            self.assertEqual(hotels[0]['hotel_id'], "H001")

        # Verify customers were created
        with open(self.customer_file, 'r', encoding='utf-8') as file:
            customers = json.load(file)
            self.assertEqual(len(customers), 2)
            self.assertEqual(customers[0]['customer_id'], "C001")

        # Verify reservations were created
        with open(self.reservation_file, 'r', encoding='utf-8') as file:
            reservations = json.load(file)
            self.assertEqual(len(reservations), 2)
            self.assertEqual(reservations[0]['reservation_id'], "R001")

        # Clean up the temporary test input file
        os.remove(input_file)


if __name__ == "__main__":
    unittest.main()
