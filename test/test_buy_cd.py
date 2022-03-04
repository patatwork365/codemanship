import unittest
import sys
print(f'sys.path : {sys.path}')

from codemanship.src.cd import CD

class PaymentService:
    pass


class Payment:
    def __init__(self, value, payment_service):
        self.value = value
        self.payment_service = payment_service


class TestBuyCD(unittest.TestCase):
    def test_buy_cd(self):
        cd = CD('', '')
        payment_service = PaymentService()
        payment = Payment(value=10, payment_service=payment_service)
        self.assertTrue(cd.buy(quantity=3, payment=payment), True)

    def test_buy_cd_if_payment_is_accepted(self):
        cd = CD('', '')
        payment_service = PaymentService()
        payment = Payment(value=10, payment_service=payment_service)
        self.assertTrue(cd.buy(quantity=1, payment=payment), True)


