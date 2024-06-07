from django_filters import filters, FilterSet

from app.models import Player


class PlayerFilter(FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    elo_rating = filters.RangeFilter(field_name='elo_rating')

    def country_filter(self, queryset, name, value):
        return queryset.filter(country__name__icontains=value)

    country = filters.CharFilter(method='country_filter', label='Country (icontains)')

    class Meta:
        model = Player
        fields = ['name', 'elo_rating', 'country']
