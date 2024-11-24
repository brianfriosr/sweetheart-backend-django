from rest_framework import viewsets
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

class ProductsView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class OrdersView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
