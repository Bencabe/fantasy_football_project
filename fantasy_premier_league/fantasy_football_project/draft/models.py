from django.db import models
from django.contrib.auth.models import User
from epl_players.models import Player
import uuid

# Create your models here.
class League(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # id = models.AutoField(primary_key=True)
    league_rep = models.ForeignKey(User,on_delete=models.CASCADE)
    league_name = models.CharField(max_length=50)
    max_teams = models.IntegerField()
    start_date = models.DateField()
    draft_date = models.DateTimeField()
    players_in_league = models.ManyToManyField(User,related_name='league_player')
    def __str__(self):
        return self.league_name

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    league = models.ForeignKey(League,on_delete=models.CASCADE)
    team_name = models.CharField(max_length=50)
    total_score = models.DecimalField(max_digits=7,decimal_places=2,default=0)
    player_1 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_1',blank=True,null=True)
    player_2 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_2',blank=True,null=True)
    player_3 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_3',blank=True,null=True)
    player_4 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_4',blank=True,null=True)
    player_5 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_5',blank=True,null=True)
    player_6 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_6',blank=True,null=True)
    player_7 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_7',blank=True,null=True)
    player_8 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_8',blank=True,null=True)
    player_9 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_9',blank=True,null=True)
    player_10 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_10',blank=True,null=True)
    player_11 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_11',blank=True,null=True)
    player_12 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_12',blank=True,null=True)
    player_13 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_13',blank=True,null=True)
    player_14 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_14',blank=True,null=True)
    player_15 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_15',blank=True,null=True)

    def __str__(self):
        return self.team_name 
    class Meta:
       unique_together = [["id", "league"],['user','league']]

# class DraftRoom(models.Model):
#     id = models.AutoField(primary_key=True)
#     league = models.ForeignKey(League,on_delete=models.CASCADE)


