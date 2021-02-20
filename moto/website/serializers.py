from rest_framework import serializers

from moto.website.models import Order


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'order_number',
            'part',
            'amount',
            'date_received',
            'date_of_expedition',
            'date_of_delivery',
            'completed_at',
            'created_at'
        )
