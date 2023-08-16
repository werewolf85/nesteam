from django.urls import path, include
from .views import *
from rest_framework import routers


urlpatterns = [
    path('list/', users_list, name='users-list'),
    path('detail/<int:pk>/', user_info, name='users-info'),
    path('players/', PlayerListAPIView.as_view(), name='players'),
    # path('user-router/', include(routers.urls)),
    path('players', PlayerListAPIView.as_view(), name='players')
]
