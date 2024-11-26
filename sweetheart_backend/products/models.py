from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()  # Cambiado a IntegerField según tu preferencia anterior
    stock = models.PositiveIntegerField()  # Cantidad disponible en inventario
    servings = models.PositiveIntegerField()  # Número de porciones
    image_url = models.URLField(max_length=500)  # URL de la imagen del producto
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()  # Campo para el correo electrónico
    address = models.TextField()
    phone = models.CharField(max_length=15)
    products = models.ManyToManyField(Product)
    total_price = models.IntegerField()  # Cambiado de DecimalField a IntegerField
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido {self.id} - {self.name}'
