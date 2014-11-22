import unittest
from cdRental.cd import CD


class TestCD(unittest.TestCase):
    def test_created_cd_object(self):
        cd = CD("CD2", "Cloud Atlas", "No")
        self.assertEqual("CD2", cd.id)
        self.assertEqual("Cloud Atlas", cd.title)
        self.assertEqual("No", cd.rented)