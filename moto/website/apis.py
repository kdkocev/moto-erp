from rest_framework.views import APIView

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    get_object_or_404
)

from moto.website.filters import OrderFilter
from moto.website.serializers import OrderListSerializer
from moto.website.models import Order


class OrderListApi(ListAPIView):
    serializer_class = OrderListSerializer
    filter_class = OrderFilter

    def get_queryset(self):
        return Order.objects.all()
