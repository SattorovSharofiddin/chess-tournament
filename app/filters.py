# filters players by name, elo_rating, and country
# filters games by result, opening_type, date_played, and player
from django_filters import filters, FilterSet, DateTimeFromToRangeFilter, widgets

from app.models import Player, Game


class PlayerFilter(FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    elo_rating = filters.NumberFilter(field_name='elo_rating')

    def country_filter(self, queryset, name, value):
        return queryset.filter(country__name__icontains=value)

    country = filters.CharFilter(method='country_filter', label='Country (icontains)')

    class Meta:
        model = Player
        fields = ['name', 'elo_rating', 'country']


class GameFilter(FilterSet):
    result = filters.CharFilter(field_name='result', lookup_expr='exact')
    opening_type = filters.CharFilter(field_name='opening_type__name', lookup_expr='icontains')
    player = filters.CharFilter(field_name='player__name', lookup_expr='icontains')

    class Meta:
        model = Game
        fields = ['result', 'opening_type', 'player']
