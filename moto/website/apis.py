from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.filters import OrderingFilter, SearchFilter

from moto.website.serializers import (
    OrderSerializer,
    PartSerializer,
    CastingSerializer,
    ExpeditionSerializer
)
from moto.website.models import Order, Part, Casting, Expedition


class OrderListCreateApi(ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = ['date_of_expedition']
    search_fields = ['number']


class OrderRetrieveUpdateApi(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class PartListCreateApi(ListCreateAPIView):
    serializer_class = PartSerializer
    queryset = Part.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = ['id']
    search_fields = ['number']


class PartRetrieveUpdateApi(RetrieveUpdateDestroyAPIView):
    serializer_class = PartSerializer
    queryset = Part.objects.all()


class CastingListCreateApi(ListCreateAPIView):
    serializer_class = CastingSerializer
    queryset = Casting.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = ['id']
    search_fields = ['number']


class CastingRetrieveUpdateApi(RetrieveUpdateDestroyAPIView):
    serializer_class = CastingSerializer
    queryset = Casting.objects.all()


class ExpeditionListCreateApi(ListCreateAPIView):
    serializer_class = ExpeditionSerializer
    queryset = Expedition.objects.all()
    filters_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = ['id']
    search_fields = ['order__number']
