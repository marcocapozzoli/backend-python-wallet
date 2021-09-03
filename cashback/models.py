from django.db import models
import decimal
from django.utils import timezone


class Customer(models.Model):
    name = models.CharField(max_length=64)
    cpf = models.CharField('CPF', max_length=11, blank=False, null=False)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    
    Category = (('A', 'Category A'), ('B', 'Category B'), ('C', 'Category C'))
    
    description = models.CharField(max_length=64, default="")
    type = models.CharField('Category', max_length=1, choices=Category, blank=False)
    price = models.FloatField(blank=False, null=False)
    quantity = models.IntegerField('Quantity', blank=False, null=False, default=1)
    
    def __str__(self):
        return self.description

class Buy(models.Model):
    customer = models.ForeignKey(Customer, related_name='customers', null=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    amount = models.FloatField('Total', blank=False, null=False)
    date = models.DateTimeField('Sale date', default=timezone.now)
    cashback = models.FloatField(blank=False, null=False)

    @staticmethod
    def get_percentage_cashback(value):
        if value > 250 and value <= 500:
            return 3.5
        elif value > 500 and value <= 1000:
            return 5.0
        elif value > 1000:
            return 8.0
        else:
            return 1.5
    
    def save(self, **kwargs):
        
        # calculate cashback
        percentage = self.get_percentage_cashback(self.amount)
        self.cashback = round((percentage / 100) * self.amount, 2)
        
        super(Buy, self).save(**kwargs)
    
    def __str__(self):
        return f'{self.amount}'


class APIMaisTodos(models.Model):
    createdAt = models.CharField(max_length=64)
    message = models.CharField(max_length=64)
    document = models.CharField(max_length=11)
    cashback_mt = models.CharField(max_length=12)
    
    def __str__(self):
        return f'{self.cashback_mt}'
