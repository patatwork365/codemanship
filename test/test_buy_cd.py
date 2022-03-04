import unittest

class CD:
    def buy(self, quantity):
        return True


class TestBuyCD(unittest.TestCase):
    def test_buy_cd(self):
        cd = CD()

        self.assertTrue(cd.buy(quantity=3), True)