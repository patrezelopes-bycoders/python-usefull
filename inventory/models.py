from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE, related_name='sale_provider')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='purchase_product')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f'{self.product} - {self.date}'

class Sale(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='sale_client')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='sale_product')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f'{self.product} - {self.date}'