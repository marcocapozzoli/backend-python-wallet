from cashback.models import Buy, Customer, Product
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from users.models import CustomUser


class BuyViewSetTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('buy-list')
        
        self.customer = Customer.objects.create(name='maistodos',cpf='69149221019')
        self.product = Product.objects.create(description='product1',type='A',price=30,quantity=1)
        self.buy = Buy.objects.create(customer=self.customer, amount=30, date='2021-09-01 10:10:10')
        self.buy.products.add(self.product)
        
        self.user = CustomUser.objects.create(username='maistodos',email='mais@todos.com',password='pythonDRF')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
    
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        
    def test_buy_list_authorized(self):
        """test that verifies that the authenticated client can access the API"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_buy_list_un_authorized(self):
        """test that verifies that the unauthenticated client can access the API"""
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_buy_create(self):
        """test that checks if the customer can create a purchase"""
        data = {
            "date": "2021-10-29 08:03:10",
            "customer":{
                "name":"maistodos",
                "cpf":"19738091098"
            },
            "products": [
                {
                    "description": "product1",
                    "type": "A",
                    "price": 100.0,
                    "quantity": 3
                }
            ],
            "amount": 300.0
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
