from rest_framework import serializers

from cashback.models import Customer, Product, Buy
from cashback.validators import validate_cpf, validate_amount


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
        extra_kwargs = {
            'date': {
                'error_messages': {
                    'invalid': 'Formato inválido para data e hora. Use o seguinte formato: YYYY-MM-DD hh:mm:ss'
                }
            }
        }        
    
    def validate(self, data):
        if not validate_cpf(data['customer']['cpf']):
            raise serializers.ValidationError(
                {'cpf': 'CPF inválido.'}
            )
        if not validate_amount(data):
            raise serializers.ValidationError(
                {'amount': 'Soma errada dos valores.'}
            )             
        return data    
    
    def create(self, validated_data):

        customer = validated_data.pop('customer')
        products = validated_data.pop('products')
        
        instance = Buy.objects.create(**validated_data)
        
        clients = Customer.objects.all()
        cpf_list = []
        for client in clients:
            cpf_list.append(client.cpf)
        
        if not customer['cpf'] in cpf_list:
            cliente_obj = Customer.objects.create(**customer)
        else:
            cliente_obj = Customer.objects.get(cpf=customer['cpf'])
            
        instance.customer = cliente_obj
        
        for product in products:
            product_obj = Product.objects.create(**product)
            instance.products.add(product_obj)                  
        
        instance.save()
                        
        return instance
    
