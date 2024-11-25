# products/urls.py
from django.urls import path, include
from rest_framework import routers
from .views import ProductsView, OrdersView
from products import views

#api versioning:
router = routers.DefaultRouter()
router.register(r'products', views.ProductsView, 'products')
router.register(r'orders', views.OrdersView, 'orders')

urlpatterns = [
    path('', include(router.urls)),
]
