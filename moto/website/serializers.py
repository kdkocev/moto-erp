from rest_framework import serializers

from moto.website.models import (
    Order,
    Part,
    Casting,
    Expedition,
    StoredCastings,
    MachinedParts
)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class CastingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casting
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class ExpeditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expedition
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class StoredCastingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoredCastings
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}

class MachinedPartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachinedParts
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}
