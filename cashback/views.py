from rest_framework import viewsets

from cashback.models import Customer, Product, Buy
from cashback.serializers import BuySerializer, ProductSerializer, CustomerSerializer


class BuyViewSet(viewsets.ModelViewSet):
    serializer_class = BuySerializer
    
    def get_queryset(self):
        buy = Buy.objects.all()
        return buy
   
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        product = Product.objects.all()
        return product
    
class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    
    def get_queryset(self):
        customer = Customer.objects.all()
        return customer
    