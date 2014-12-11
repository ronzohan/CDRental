import unittest
from cdRental.clerk import Clerk
from cdRental.customer import Customer
from cdRental.cd import CD
from cdRental.cd_rental_app import CDLIST, CUSTOMERLIST


class TestClerk(unittest.TestCase):
    def test_clerk_checkout(self):
        cd = CD("CD2", "Cloud Atlas", "No", rental_period=2)
        CDLIST.add_cd(cd)

        customer = Customer(001, "Ron")
        CUSTOMERLIST.add_customer(customer)
        
        clerk = Clerk()
        clerk.record_cd_as_rented(cd.id, customer.id)
        self.assertEqual(CDLIST.get_cd_data(cd.id).rented, "Yes")

    def test_generate_rental_contract(self):
        clerk = Clerk()
        rental_contract = clerk.generate_rental_contract("CD2")
        self.assertEqual(rental_contract.get('CDID'), "CD2")
        