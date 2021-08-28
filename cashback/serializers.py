from rest_framework import serializers
from cashback.models import Customer, Product, Buy


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'cpf']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['description', 'type', 'price', 'quantity']

class BuySerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    products = ProductSerializer(many=True)
    cashback = serializers.ReadOnlyField()

    class Meta:
        model = Buy
        fields = ['id', 'date', 'customer', 'products', 'amount', 'cashback']