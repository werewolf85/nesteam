from django_filters import rest_framework as filters
from .models import Game
import django_filters

class GameFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    year = django_filters.CharFilter(lookup_expr='icontains')
    year__gt = django_filters.NumberFilter(field_name='year', lookup_expr='gt')
    year__lt = django_filters.NumberFilter(field_name='year', lookup_expr='lt')
    genre = django_filters.CharFilter(lookup_expr='icontains')
    studio = django_filters.CharFilter(lookup_expr='icontains')
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    class Meta:
        model = Game
        fields = ['name', 'year', 'genre', 'studio']