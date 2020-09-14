# Generated by Django 3.0.3 on 2020-08-27 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('epl_players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('max_teams', models.IntegerField()),
                ('start_date', models.DateField()),
                ('draft_date', models.DateTimeField()),
                ('league_rep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('total_score', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='draft.League')),
                ('player_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_1', to='epl_players.Player')),
                ('player_10', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_10', to='epl_players.Player')),
                ('player_11', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_11', to='epl_players.Player')),
                ('player_12', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_12', to='epl_players.Player')),
                ('player_13', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_13', to='epl_players.Player')),
                ('player_14', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_14', to='epl_players.Player')),
                ('player_15', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_15', to='epl_players.Player')),
                ('player_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_2', to='epl_players.Player')),
                ('player_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_3', to='epl_players.Player')),
                ('player_4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_4', to='epl_players.Player')),
                ('player_5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_5', to='epl_players.Player')),
                ('player_6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_6', to='epl_players.Player')),
                ('player_7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_7', to='epl_players.Player')),
                ('player_8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_8', to='epl_players.Player')),
                ('player_9', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_9', to='epl_players.Player')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('id', 'league')},
            },
        ),
    ]