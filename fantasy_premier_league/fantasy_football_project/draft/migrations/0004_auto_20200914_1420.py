# Generated by Django 3.0.3 on 2020-09-14 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('epl_players', '0002_player_cur_score'),
        ('draft', '0003_league_players_in_league'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='player_1',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_1', to='epl_players.Player'),
        ),
        migrations.AlterField(
            model_name='team',
            name='player_10',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_10', to='epl_players.Player'),
        ),
        migrations.AlterField(
            model_name='team',
            name='player_11',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_11', to='epl_players.Player'),
        ),
        migrations.AlterField(
            model_name='team',
            name='player_12',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_12', to='epl_players.Player'),
        ),
        migrations.AlterField(
            model_name='team',
            name='player_13',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_13', to='epl_players.Player'),
        ),
        migrations.AlterField(
            model_name='team',
            name='player_14',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_14', to='epl_players.Player'),
        ),
        migrations.AlterField(
            model_name='team',
            name='player_15',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_15', to='epl_players.Player'),
        ),
        migrations.AlterField(
            model_name='team',
            name='player_2',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_2', to='epl_players.Player'),
        ),
        migrations.AlterField(
            model_name='team',
            name='player_3',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_3', to='epl_players.Player'),
        ),
        migrations.AlterField(
            model_name='team',
            name='player_4',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_4', to='epl_players.Player'),
        ),
        migrations.AlterField(
            model_name='team',
            name='player_5',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_5', to='epl_players.Player'),
        ),
        migrations.AlterField(
            model_name='team',
            name='player_6',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_6', to='epl_players.Player'),
        ),
        migrations.AlterField(
            model_name='team',
            name='player_7',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_7', to='epl_players.Player'),
        ),
        migrations.AlterField(
            model_name='team',
            name='player_8',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_8', to='epl_players.Player'),
        ),
        migrations.AlterField(
            model_name='team',
            name='player_9',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_9', to='epl_players.Player'),
        ),
        migrations.AlterUniqueTogether(
            name='team',
            unique_together={('id', 'league'), ('user', 'league')},
        ),
    ]