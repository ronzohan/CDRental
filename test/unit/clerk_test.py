import unittest
from cdRental.clerk import Clerk

class TestClerk(unittest.TestCase):
    def test_clerk_checkout(self):
        clerk = Clerk()