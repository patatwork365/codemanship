import unittest

from src.cd import CD


class TestBuyCD(unittest.TestCase):
    def test_buy_cd(self):
        cd = CD('', '')

        self.assertTrue(cd.buy(quantity=3), True)
