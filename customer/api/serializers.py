from rest_framework import serializers

from customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer

        fields = [
            'owner',
            'company',
            'address',
            'mobile_no',
            'phone_no',
            'email',
            'pan_no',
        ]
