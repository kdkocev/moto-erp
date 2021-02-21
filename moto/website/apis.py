from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView
)

from moto.website.filters import OrderFilter
from moto.website.serializers import OrderSerializer, PartSerializer, CastingSerializer
from moto.website.models import Order, Part, Casting


class OrderListCreateApi(ListCreateAPIView):
    serializer_class = OrderSerializer
    filter_class = OrderFilter
    queryset = Order.objects.all()


class OrderRetrieveUpdateApi(RetrieveUpdateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class PartListCreateApi(ListCreateAPIView):
    serializer_class = PartSerializer
    queryset = Part.objects.all()


class PartRetrieveUpdateApi(RetrieveUpdateAPIView):
    serializer_class = PartSerializer
    queryset = Part.objects.all()


class CastingListCreateApi(ListCreateAPIView):
    serializer_class = CastingSerializer
    queryset = Casting.objects.all()


class CastingRetrieveUpdateApi(RetrieveUpdateAPIView):
    serializer_class = CastingSerializer
    queryset = Casting.objects.all()
