from django.db import models

# Create your models here.
class Player(models.Model):
    nick = models.CharField(max_length=55)