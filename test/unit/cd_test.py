import unittest
from cdRental.cd import CD
from cdRental.customer import Customer
import datetime


class TestCD(unittest.TestCase):
    def test_created_cd_object(self):
        cd = CD("CD2", "Cloud Atlas", "No", rental_period=2)
        self.assertEqual("CD2", cd.id)
        self.assertEqual("Cloud Atlas", cd.title)
        self.assertEqual("No", cd.rented)

    def test_rent_on_cd(self):
        cd = CD("CD2", "Cloud Atlas", "No", rental_period=2)
        customer = Customer(001, "Ron Darl Magno")
        cd.set_rent(customer)
        self.assertEqual(cd.rented, "Yes")

        rental_due = datetime.date.today() + \
            datetime.timedelta(days=cd.rental_period)
        rental_due = rental_due.strftime("%m/%d/%Y") 

        self.assertEqual(cd.rental_due, rental_due)
        self.assertEqual(cd.customer_id, 001)
