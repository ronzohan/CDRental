import unittest
from cdRental.cd_stock import CDStock
from cdRental.cd import CD


class TestCDStock(unittest.TestCase):
    def test_adding_cd_data_to_cd_stock_object(self):
        cd1 = CD(001, "Cloud Atlas", "No")
        cd2 = CD(002, "King of Summer", "No")
        cd_stock = CDStock()
        cd_stock.add_cd(cd1)
        cd_stock.add_cd(cd2)

        self.assertEqual(len(cd_stock.cds), 2)

    def test_retrieve_cd_data(self):
        cd1 = CD(001, "Cloud Atlas", "No")
        cd_stock = CDStock()
        cd_stock.add_cd(cd1)

        self.assertEqual(cd_stock.get_cd_data(001), cd1)
        
