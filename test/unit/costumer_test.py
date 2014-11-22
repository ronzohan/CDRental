import unittest
from cdRental.customer import Customer


class TestCostumer(unittest.TestCase):
    def test_create_a_customer(self):
        customer = Customer(001, "Ron Daryl Magno")

    