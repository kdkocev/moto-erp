import django_filters

from moto.website.models import Order


class OrderFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search')

    def filter_search(self, queryset, name, value):
        return queryset

    class Meta:
        model = Order
        fields = ()
