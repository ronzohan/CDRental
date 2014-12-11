import unittest
from cdRental.cd_list import CDList
from cdRental.cd import CD


class TestCDStock(unittest.TestCase):
    def test_adding_cd_data_to_cd_stock_object(self):
        cd1 = CD(001, "Cloud Atlas", "No", rental_period=2)
        cd2 = CD(002, "King of Summer", "No", rental_period=1)
        cd_list = CDList()
        cd_list.add_cd(cd1)
        cd_list.add_cd(cd2)

        self.assertEqual(len(cd_list.cds), 2)

    def test_retrieve_cd_data(self):
        cd1 = CD(001, "Cloud Atlas", "No", rental_period=1)
        cd_list = CDList()
        cd_list.add_cd(cd1)

        self.assertEqual(cd_list.get_cd_data(001), cd1)
        self.assertEqual(cd_list.get_cd_data(002), None)
