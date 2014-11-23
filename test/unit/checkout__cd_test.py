import unittest
from cdRental.checkout_cd import CheckoutCD
from cdRental.customer import Customer
from cdRental.cd import CD


class TestCheckoutCD(unittest.TestCase):
    def test_checkout_a_cd(self):
        customer = Customer(001, "Ron Daryl Magno")
        cd = CD("CD2", "Cloud Atlas", "No", rental_period=2)
        checkout_cd = CheckoutCD()
        checkout_cd.checkout(customer, cd)
        self.assertEqual(checkout_cd.customer, customer)
        self.assertEqual(checkout_cd.cd.rented, "Yes")

    def test_check_if_customer_and_cd_objects_are_valid(self):
        customer = 1
        cd = 2
        checkout_cd = CheckoutCD()
        self.assertRaises(TypeError, checkout_cd.checkout, customer, cd)