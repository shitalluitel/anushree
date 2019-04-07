from rest_framework import serializers
from sliderimages.models import SliderImage


class SliderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderImage

        fields = [
            'id',
            'name',
            'image',
            'description'
        ]

