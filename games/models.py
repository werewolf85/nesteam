from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=255)
    year = models.PositiveIntegerField()

    def __srt__(self):
        return self.name

class Studio(models.Model):
    name = models.CharField(max_length=255)
    workers_count = models.IntegerField()
    games_count = models.PositiveIntegerField()

    def __srt__(self):
        return self.name