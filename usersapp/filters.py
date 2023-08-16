from django_filters import rest_framework as filters
from .models import Player
import django_filters

class PlayerFilter(filters.FilterSet):
    nick = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Player
        fields = ['nick']