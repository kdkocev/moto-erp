from rest_framework import serializers

from moto.website.models import Order, Part, Casting, Expedition


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.order_number = validated_data.get('order_number', instance.order_number)
        instance.part = validated_data.get('part', instance.part)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.date_received = validated_data.get('date_received', instance.date_received)
        instance.date_of_expedition = validated_data.get('date_of_expedition', instance.date_of_expedition)
        instance.date_of_delivery = validated_data.get('date_of_delivery', instance.date_of_delivery)
        instance.completed_at = validated_data.get('completed_at', instance.completed_at)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()

        return instance


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        return Part.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.number = validated_data.get('number', instance.number)
        instance.price_total = validated_data.get('price_total', instance.price_total)
        instance.price_machining = validated_data.get('price_machining', instance.price_machining)
        instance.casting = validated_data.get('casting', instance.casting)
        instance.save()

        return instance


class CastingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casting
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        return Casting.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.number = validated_data.get('number', instance.number)
        instance.save()

        return instance


class ExpeditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expedition
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}
