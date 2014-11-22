import unittest
from cdRental.customer import Customer
from cdRental.cd import CD


class TestCostumer(unittest.TestCase):
    def test_customer_returns_customer_data(self):
        customer = Customer(001, "Ron Daryl")
        self.assertEqual(customer.name, "Ron Daryl")