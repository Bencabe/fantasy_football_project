# Generated by Django 3.0.3 on 2020-09-10 09:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('draft', '0002_auto_20200908_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='players_in_league',
            field=models.ManyToManyField(related_name='league_player', to=settings.AUTH_USER_MODEL),
        ),
    ]
