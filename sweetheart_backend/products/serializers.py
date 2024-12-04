from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    product_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Product.objects.all()
    )
    updated_product = serializers.DictField(write_only=True, required=False)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        # Lógica existente para crear una orden
        product_ids = validated_data.pop('product_ids', [])
        updated_product = validated_data.pop('updated_product', {})
        product_ids = [p.id if isinstance(p, Product) else p for p in product_ids]
        order = Order.objects.create(**validated_data)
        order.products.set(product_ids)

        if updated_product and product_ids:
            product_id = product_ids[0]
            try:
                product = Product.objects.get(id=product_id)
                product.servings = updated_product.get('servings', product.servings)
                product.price = updated_product.get('price', product.price)
                product.save()
            except Product.DoesNotExist:
                print(f"El producto con ID {product_id} no existe.")
        return order

    def update(self, instance, validated_data):
        # Logs para depuración
        print("Datos validados para la actualización:", validated_data)

        # Actualizar campos de la orden
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.total_price = validated_data.get('total_price', instance.total_price)

        # Si se proporcionaron nuevos productos, actualizarlos
        product_ids = validated_data.pop('product_ids', None)
        if product_ids:
            product_ids = [p.id if isinstance(p, Product) else p for p in product_ids]
            instance.products.set(product_ids)
            print("Productos actualizados en la orden:", instance.products.all())

        # Guardar cambios en la orden
        instance.save()

        return instance
