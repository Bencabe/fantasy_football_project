# Generated by Django 3.0.3 on 2020-09-14 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0007_auto_20200914_1426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='league',
            old_name='name',
            new_name='league_name',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='name',
            new_name='team_name',
        ),
    ]