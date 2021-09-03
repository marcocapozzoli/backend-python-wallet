from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from cashback.api import call_api_maisTodos

from cashback.models import Customer, Product, Buy
from cashback.serializers import BuySerializer, ProductSerializer, CustomerSerializer


class BuyViewSet(viewsets.ModelViewSet):
    queryset = Buy.objects.all()
    serializer_class = BuySerializer    
       
    def create(self, request, *args, **kwargs):
        serializer = BuySerializer(data=request.data)
        serializer.is_valid(self)
        serializer.save()
        
        buys = self.queryset.order_by('-id')
        last_buy = buys[0]
        document = last_buy.customer.cpf
        cashback = last_buy.cashback
        
        #response_api_maisTodos = call_api_maisTodos(document,cashback)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
   
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
    