# Generated by Django 4.2.4 on 2023-08-15 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_game_studio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='year',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
