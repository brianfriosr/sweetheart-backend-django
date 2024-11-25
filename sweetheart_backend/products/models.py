# models.py
from django.db import models

# models.py
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()  # Cambiado de DecimalField a IntegerField
    stock = models.PositiveIntegerField(null=True)
    servings = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    products = models.ManyToManyField(Product)
    total_price = models.IntegerField()  # Cambiado de DecimalField a IntegerField
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido {self.id} - {self.name}'
