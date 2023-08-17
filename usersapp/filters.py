from django_filters import rest_framework as filters
from .models import Player
import django_filters

class PlayerFilter(filters.FilterSet):
    nick = django_filters.CharFilter(lookup_expr='icontains')
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    class Meta:
        model = Player
        fields = ['nick']