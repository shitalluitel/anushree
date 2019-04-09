from rest_framework import serializers

from products.models import Product


class TubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = [
            'id',
            'pattern_name',
            'pattern_code',
            'size',
            # 'category',
            # 'product_name',
            'stock',
            'price',
        ]

        extra_kwargs = {'password': {'read_only': True}}


class TireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = [
            'id',
            'size',
            'product_name',
            # 'category',
            'pr',
            'stock',
            'price',
        ]

        extra_kwargs = {'password': {'read_only': True}}


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = [
            'pattern_name',
            'pattern_code',
            'size',
            'size',
            'product_name',
            'pr',
            'stock',
            'price',
        ]
