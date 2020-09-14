from django.db import models
from django.contrib.auth.models import User
from epl_players.models import Player
import uuid

# Create your models here.
class League(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # id = models.AutoField(primary_key=True)
    league_rep = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    max_teams = models.IntegerField()
    start_date = models.DateField()
    draft_date = models.DateTimeField()
    players_in_league = models.ManyToManyField(User,related_name='league_player')
    def __str__(self):
        return self.name

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    league = models.ForeignKey(League,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    total_score = models.DecimalField(max_digits=7,decimal_places=2,default=0)
    player_1 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_1')
    player_2 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_2')
    player_3 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_3')
    player_4 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_4')
    player_5 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_5')
    player_6 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_6')
    player_7 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_7')
    player_8 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_8')
    player_9 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_9')
    player_10 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_10')
    player_11 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_11')
    player_12 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_12')
    player_13 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_13')
    player_14 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_14')
    player_15 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='player_15')

    def __str__(self):
        return self.name 
    class Meta:
       unique_together = [["id", "league"]]

# class DraftRoom(models.Model):
#     id = models.AutoField(primary_key=True)
#     league = models.ForeignKey(League,on_delete=models.CASCADE)


