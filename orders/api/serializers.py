from rest_framework import serializers

from orders.models import Cart, CartItem, Order, OrderItem
from products.api.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    """Serializer for the Cart model."""

    # used to represent the target of the relationship using its __unicode__ method
    items = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cart
        fields = (
            'id', 'items'
        )


class CartItemSerializer(serializers.ModelSerializer):
    """Serializer for the CartItem model."""

    cart = CartSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = (
            'id', 'cart', 'product', 'quantity'
        )


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for the Order model."""

    # used to represent the target of the relationship using its __unicode__ method
    order_items = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Order
        fields = (
            'id', 'total', 'order_items'
        )

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        return order


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for the OrderItem model."""

    order = OrderSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = (
            'id', 'order', 'product', 'quantity'
        )
