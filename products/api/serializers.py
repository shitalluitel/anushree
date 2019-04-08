from rest_framework import serializers

from products.models import Product


#
# class TireSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#
#         fields = [
#
#         ]


class TubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = [
            'pattern_name',
            'pattern_code',
            'size',
            # 'category',
            # 'product_name',
            'stock',
            'price',
        ]


class TireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = [
            'size',
            'product_name',
            # 'category',
            'pr',
            'stock',
            'price',
        ]


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
