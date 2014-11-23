import unittest
from cdRental.customer_list import CustomerList
from cdRental.customer import Customer


class TestCustomerList(unittest.TestCase):
    def test_add_customer_in_customer_list(self):
        customer1 = Customer(001, "Ron Daryl Magno")
        customer2 = Customer(002, "Ron Daryl Magnos")

        customer_list = CustomerList()

        customer_list.add_customer(customer1)
        customer_list.add_customer(customer2)

        self.assertEqual(len(customer_list.list), 2)

    def test_get_customer_data(self):
        customer1 = Customer(001, "Ron Daryl Magno")

        customer_list = CustomerList()

        customer_list.add_customer(customer1)

        self.assertEqual(customer_list.get_customer_data(001), customer1)
        self.assertEqual(customer_list.get_customer_data(002), None)

    def test_get_customer_data_given_id_is_string(self):
        customer1 = Customer("001", "Ron Daryl Magno")
        customer_list = CustomerList()
        customer_list.add_customer(customer1)
        self.assertEqual(customer_list.get_customer_data("001").id, customer1.id)
