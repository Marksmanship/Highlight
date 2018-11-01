from django.db import models
from django.contrib.auth.models import User
from scholarship_map.models import Sport
SF = "Small Forward"
PF = "Point Forward"
PG = "Point Guard"
SG = "Shooting Guard"
C = "Center"
S = "Swingman"
PTF = "Point Forward"
FC = "Forward Center"
# Create your models here.
class Basketball(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    user = models.ForeignKey(User, related_name='user_sport')# get_user_model.obj
    sport_name = models.ForeignKey(Sport)
    position = models.CharField(max_length=100,choices=(
        (SF, "Small Forward"),
        (PF, "Point Forward"),
        (PG, "Point Guard"),
        (SG, "Shooting Guard"),
        (C, "Center"),
        (S, "Swingman"),
        (PTF, "Point Forward"),
        (FC, "Forward Center"),
    ))
    points = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    timeouts = models.IntegerField(default=0)

# Going to
#
