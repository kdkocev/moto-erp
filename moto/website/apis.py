from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    get_object_or_404
)

from moto.website.filters import OrderFilter
from moto.website.serializers import OrderListSerializer, OrderDetailsSerializer
from moto.website.models import Order


class OrderListApi(ListAPIView):
    serializer_class = OrderListSerializer
    filter_class = OrderFilter

    def get_queryset(self):
        return Order.objects.all()


class OrderDetailApi(APIView):
    def get(self, request, order_id):
      order = get_object_or_404(Order, id=order_id)

      return Response(OrderDetailsSerializer(order).data)
