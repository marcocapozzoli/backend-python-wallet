from cashback.models import Buy, Customer, Product
from rest_framework.test import APITestCase

  
class BuyTestCase(APITestCase):
            
    def test_buy_cashback_rule_15(self):
        """test that checks the 1.5% cashback rule"""
        buy = Buy(amount=100)
        buy.save()
        cashback = buy.cashback
        self.assertEqual(cashback, round((1.5 / 100 * buy.amount), 2))
    
    def test_buy_cashback_rule_35(self):
        """test that checks the 3.5% cashback rule"""
        buy = Buy(amount=300)
        buy.save()
        cashback = buy.cashback
        self.assertEqual(cashback, round((3.5 / 100 * buy.amount), 2))
    
    def test_buy_cashback_rule_50(self):
        """test that checks the 5% cashback rule"""
        buy = Buy(amount=600)
        buy.save()
        cashback = buy.cashback
        self.assertEqual(cashback, round((5 / 100 * buy.amount), 2))
    
    def test_buy_cashback_rule_80(self):
        """test that checks the 8% cashback rule"""
        buy = Buy(amount=1200)
        buy.save()
        cashback = buy.cashback
        self.assertEqual(cashback, round((8 / 100 * buy.amount), 2))
        
