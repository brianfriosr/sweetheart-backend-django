from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    # Relación ManyToMany
    products = ProductSerializer(many=True, read_only=True)  # Para mostrar los productos relacionados
    product_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Product.objects.all()
    )  # Para recibir los IDs de productos al crear un pedido

    class Meta:
        model = Order
        fields = ['id', 'name', 'address', 'phone', 'products', 'product_ids', 'total_price', 'created_at']

def create(self, validated_data):
    # Extraemos los IDs de los productos del diccionario de datos validados
    # `pop` elimina la clave 'product_ids' del diccionario y la guarda en `product_ids`
    # Si no encuentra 'product_ids', devuelve una lista vacía por defecto.
    product_ids = validated_data.pop('product_ids', [])
    
    # Usamos el operador ** para desempaquetar los datos validados y pasarlos como argumentos
    # clave-valor al método `Order.objects.create()`. Esto crea un nuevo objeto `Order`
    # utilizando los datos del diccionario `validated_data`, excluyendo 'product_ids'
    order = Order.objects.create(**validated_data)

    # Asignamos los productos al pedido usando la relación ManyToMany.
    # `product_ids` es una lista de los IDs de productos seleccionados,
    # y `order.products.set(product_ids)` asocia esos productos con el pedido recién creado.
    order.products.set(product_ids)

    # Devolvemos el objeto `order` recién creado
    return order

