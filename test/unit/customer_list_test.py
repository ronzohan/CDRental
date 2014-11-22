import unittest
from cdRental.customer_list import CustomerList
from cdRental.customer import Customer


class TestCustomerList(unittest.TestCase):
    def test_add_customer_in_customer_list(self):
        customer1 = Customer(001, "Ron Daryl Magno")
        customer_list = CustomerList()
        customer_list.add_customer(customer1)