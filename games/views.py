from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

def games_list(request):
    game_lst = Game.objects.all()
    serializer = GameSerializer(game_lst, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)


class StudiosListAPIView(ListAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer


class StudioViewSet(ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

# def studios_list(request):
#     studios_lst = Studio.objects.all()
#     serializer = StudioSerializer(studios_lst, many=True)
#     data = serializer.data
#     return JsonResponse(data, safe=False)

# class CreateGameAPIView(CreateAPIView):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializer

class GamesView(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer