from django.db import models

# Create your models here.
class Player(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    total_score = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    cur_score = models.DecimalField(max_digits=3,decimal_places=2,default=0)
    football_team = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' +self.last_name
