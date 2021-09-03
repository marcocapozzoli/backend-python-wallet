from cashback.models import Buy, Customer, Product
from cashback.serializers import (BuySerializer, CustomerSerializer,
                                  ProductSerializer)
from rest_framework.test import APITestCase


class CustomerSerializerTestCase(APITestCase):
    
    def setUp(self):
        self.customer_attributes = {
            "name":"maistodos",
            "cpf":"07268305001"
        }
        self.customer = Customer.objects.create(**self.customer_attributes)
        self.serializer = CustomerSerializer(instance=self.customer)
    
    def test_customer_contains_expected_fields(self):
        """test that verifies that fields are being serialized correctly"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['name', 'cpf']))

    def test_customer_fields_content(self):
        """test that verifies that the contents of serialized fields are correct"""
        data = self.serializer.data
        self.assertEqual(data['name'], self.customer.name)
        self.assertEqual(data['cpf'], self.customer.cpf)

class ProductSerializerTestCase(APITestCase):
    
    def setUp(self):
        self.product_attributes = {
            "description": "product1",
            "type": "A",
            "price": 100.55,
            "quantity": 1
        }
        self.product = Product.objects.create(**self.product_attributes)
        self.serializer = ProductSerializer(instance=self.product)
            
    def test_product_contains_expected_fields(self):
        """test that verifies that fields are being serialized correctly"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['description', 'type', 'price', 'quantity']))

    def test_product_fields_content(self):
        """test that verifies that the contents of serialized fields are correct"""
        data = self.serializer.data
        self.assertEqual(data['description'], self.product.description)
        self.assertEqual(data['type'], self.product.type)
        self.assertEqual(data['price'], self.product.price)
        self.assertEqual(data['quantity'], self.product.quantity)

class BuySerializerTestCase(APITestCase):
    
    def setUp(self):
        self.customer_attributes = {
            "name":"maistodos",
            "cpf":"30314608044"
        }
        self.product_attributes = {
            "description": "product1",
            "type": "A",
            "price": 100.55,
            "quantity": 1
        }       
        self.buy_attributes = {
            "date": "2021-10-29 08:03:10",
            "amount": 100.55
        }
        self.customer = Customer.objects.create(**self.customer_attributes)
        self.product = Product.objects.create(**self.product_attributes)
        self.buy = Buy.objects.create(**self.buy_attributes)
        self.buy.customer = self.customer
        self.buy.products.add(self.product)
        self.serializer = BuySerializer(instance=self.buy)
    
    def test_buy_contains_expected_fields(self):
        """test that verifies that fields are being serialized correctly"""
        data = self.serializer.data
        
        self.assertEqual(set(data.keys()), set(['id','date','customer','products','amount','cashback']))

    def test_buy_fields_content(self):
        """test that verifies that the contents of serialized fields are correct"""
        data = self.serializer.data
        
        for product in data['products']:
            data_product = product
        
        self.assertEqual(data['date'], self.buy.date)
        self.assertEqual(data['customer'], self.customer_attributes)
        self.assertEqual(data_product, self.product_attributes)
        self.assertEqual(data['amount'], self.buy.amount)
        self.assertEqual(data['cashback'], self.buy.cashback)

    def test_buy_wrong_validate_cpf(self):
        """test that checks the validation of the invalid cpf"""
        data = {
            "customer":{
                "name":"maistodos",
                "cpf":"00000000000"
            },
            "products":[],
            "amount":0
        }
        serializer = BuySerializer(data=data)
        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(set(serializer.errors.keys()), set(['cpf']))
        
    def test_buy_correct_validate_cpf(self):
        """test that checks the validation of valid cpf"""
        data = {
            "customer":{
                "name":"maistodos",
                "cpf":"40495330060"
            },
            "products":[],
            "amount": 0
        }
        serializer = BuySerializer(data=data)
        self.assertEqual(serializer.is_valid(), True)
