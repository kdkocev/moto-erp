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
    ExpeditionSerializer,
    StoredCastingsSerializer,
    MachinedPartsSerializer
)
from moto.website.models import (
    Order,
    Part,
    Casting,
    Expedition,
    StoredCastings,
    MachinedParts
)


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
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    ordering = ['date_of_expedition']
    search_fields = ['order__number']


class ExpeditionRetrieveUpdateApi(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpeditionSerializer
    queryset = Expedition.objects.all()


class StoredCastingsListCreateApi(ListCreateAPIView):
    serializer_class = StoredCastingsSerializer
    queryset = StoredCastings.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fieds = '__all__'
    ordering_fields = '__all__'
    ordering = ['created_at']
    search_fields = ['casting__number']


class StoredCastingsRetrieveUpdateApi(RetrieveUpdateDestroyAPIView):
    serializer_class = StoredCastingsSerializer
    queryset = StoredCastings.objects.all()


class MachinedPartsListCreateApi(ListCreateAPIView):
    serializer_class = MachinedPartsSerializer
    queryset = MachinedParts.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fieds = '__all__'
    ordering_fields = '__all__'
    ordering = ['created_at']
    search_fields = ['part__number']


class MachinedPartsRetrieveUpdateApi(RetrieveUpdateDestroyAPIView):
    serializer_class = MachinedPartsSerializer
    queryset = MachinedParts.objects.all()
