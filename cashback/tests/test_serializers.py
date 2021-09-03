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
