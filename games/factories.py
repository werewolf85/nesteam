import factory
from .models import Genre, Game, Studio

class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre

    name = factory.Sequence(
        lambda n: f'Test genre {n}'
    )

class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Game

    name = factory.Sequence(
        lambda n: f'Test game {n}'
    )

class StudioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Studio

    name = factory.Sequence(
        lambda n: f'Test studio {n}'
    )