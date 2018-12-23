# This file doesn't cause the 0 Primary Key erorr
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

from scholarship_map.models import Sport


# Create your models here.
class Basketball(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(), related_name='rn_user_basketball', on_delete=models.CASCADE)# get_user_model.obj
    position = models.CharField(max_length=40,choices=(
        ('SMALL_FORWARD', "Small Forward"),
        ('POINT_FORWARD', "Point Forward"),
        ('POINT_GUARD', "Point Guard"),
        ('SHOOTING_GUARD', "Shooting Guard"),
        ('CENTER', "Center"),
        ('WING', "Wing"),
        ('POINT_FORWARD', "Point Forward"),
        ('FORWARD_CENTER', "Forward Center"),
    ))
    points = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    timeouts = models.IntegerField(default=0)

class Soccer(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(), related_name='rn_user_Soccer', on_delete=models.CASCADE)
    position = models.CharField(max_length=100,choices=(
        ('FORWARD', "Forward"),
        ('RIGHT_BACK', "Right Back Fielder"),
        ('RIGHT_MID', "Right Mid Fielder"),
        ('LEFT_MID', "Left Mid Fielder"),
        ('LEFT_BACK', "Left Back Fielder"),
        ('DEFENSIVE_MID', "Defensive Mid Fielder"),
        ('GOALKEEPER', "Goalkeeper"),
        ('STRIKER', "Striker"),
        ('SWEEPER', "Sweeper"),
        ('STOPPER', "Stopper"),
    ))
    points = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    timeouts = models.IntegerField(default=0)
# Going to
#
