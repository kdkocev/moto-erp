from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView
)

from moto.website.filters import OrderFilter
from moto.website.serializers import OrderSerializer, PartSerializer
from moto.website.models import Order, Part


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
