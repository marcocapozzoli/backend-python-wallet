from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=64)
    cpf = models.CharField('CPF', max_length=11, blank=False, null=False)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    
    Category = (('A', 'Category A'), ('B', 'Category B'), ('C', 'Category C'))
    
    description = models.CharField(max_length=64, default="")
    type = models.CharField('Category', max_length=1, choices=Category, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField('Quantity', blank=False, null=False, default=1)
    
    def __str__(self):
        return self.description

class Buy(models.Model):
    customer = models.ForeignKey(Customer, related_name='customers', null=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    amount = models.DecimalField('Total', max_digits=8, decimal_places=2, blank=True, null=True)
    date = models.DateTimeField('Sale date')
    cash = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.amount


class APIMaisTodos(models.Model):
    createdAt = models.CharField(max_length=64)
    message = models.CharField(max_length=64)
    document = models.CharField(max_length=11)
    cashback = models.CharField(max_length=12)
    
    def __str__(self):
        return self.cashback
