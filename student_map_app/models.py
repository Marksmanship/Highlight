# This file doesn't cause the 0 Primary Key erorr
from django.conf import settings
from django.db import models

from athlete_and_school_app.models import Sport

# settings.AUTH_USER_MODEL.rn_user_basketball.create(request.POST) // Create a baskeball instance that references the current user and populate it with POST
# User.objects.filter(username=request.user).rn_user_basketball.all() // Get all basketball instances that references the current user
# How will we handle junior varsity and varsity teams?
class Baseball(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    YEAR_CHOICES = (
        ('FRESHMAN','Freshman Year'),
        ('SOPHMORE','Sophmore Year'),
        ('JUNIOR','Junior Year'),
        ('SENIOR','Senior Year'),
    )
    year = models.CharField(choices=YEAR_CHOICES, default=YEAR_CHOICES[0][0], null=False, max_length=20)
    position = models.CharField(max_length=100,choices=(
        ('C', "Catcher"),
        ('CF', "Center Fielder"),
        ('CL', "Closer"),
        ('DH', "Designated Hitter"),
        ('1B', "First Baseman"),
        ('IF', "Infielder"),
        ('LF', "Left Fielder"),
        ('LHS', "Left-handed Specialist"),
        ('P', "Pitcher"),
        ('RF', "Right Fielder"),
        ('2B', "Second Baseman"),
        ('SS', "Shortstop"),
        ('SP', "Starting Pitcher"),
        ('3B', "Third Baseman"),
        ('UI', "Utility Infielder"),
        ('UP', "Utility Players"),
    ))
    games = models.IntegerField(default=0)
    runs = models.IntegerField(default=0)
    runs_batted_in = models.IntegerField(default=0)
    single_hits = models.IntegerField(default=0)
    double_hits = models.IntegerField(default=0)
    tripple_hits = models.IntegerField(default=0)
    home_runs = models.IntegerField(default=0)
    stolen_bases = models.IntegerField(default=0)
    bases_on_ball = models.IntegerField(default=0)
    strikeouts = models.IntegerField(default=0)

    def get_sport_name(self):
        return "Baseball"
    class Meta:
        unique_together = ('year', 'user')

class Basketball(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)# get_user_model.obj
    YEAR_CHOICES = (
        ('FRESHMAN','Freshman Year'),
        ('SOPHMORE','Sophmore Year'),
        ('JUNIOR','Junior Year'),
        ('SENIOR','Senior Year'),
    )
    year = models.CharField(choices=YEAR_CHOICES, default=YEAR_CHOICES[0][0], null=False, max_length=20)
    position = models.CharField(max_length=30,choices=(
        ('SF', "Small Forward"),
        ('PF', "Point Forward"),
        ('PG', "Point Guard"),
        ('SG', "Shooting Guard"),
        ('C', "Center"),
        ('W', "Wing"),
        ('PF', "Point Forward"),
        ('FC', "Forward Center"),
    ))
    dunks = models.IntegerField(default=0)
    two_pointers = models.IntegerField(default=0)
    three_pointers = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    timeouts = models.IntegerField(default=0)

    def get_sport_name(self):
        return "Basketball"

    class Meta:
        unique_together = ('year', 'user')

class Bowling(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)# get_user_model.obj
    YEAR_CHOICES = (
        ('FRESHMAN YEAR','Freshman Year'),
        ('SOPHMORE YEAR','Sophmore Year'),
        ('JUNIOR YEAR','Junior Year'),
        ('SENIOR YEAR','Senior Year'),
    )
    year = models.CharField(choices=YEAR_CHOICES, default=YEAR_CHOICES[0][0], null=False, max_length=20)
    position = models.CharField(max_length=30,choices=(
        ('LEFT_HANDED', "Left-handed"),
        ('RIGHT_HANDED', "Right-handed"),
    ))
    points = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    timeouts = models.IntegerField(default=0)

    def get_sport_name(self):
        return "Bowling"

    class Meta:
        unique_together = ('year', 'user')

class Cheerleading(models.Model):           # Don't store any stats, have cheerleaders upload video clips instead
    pass
class Cross_Country(models.Model):          # More of a team-based sport. Should we store this?
    pass


class Field_Hockey(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)# get_user_model.obj
    YEAR_CHOICES = (
        ('FRESHMAN YEAR','Freshman Year'),
        ('SOPHMORE YEAR','Sophmore Year'),
        ('JUNIOR YEAR','Junior Year'),
        ('SENIOR YEAR','Senior Year'),
    )
    year = models.CharField(choices=YEAR_CHOICES, default=YEAR_CHOICES[0][0], null=False, max_length=20)
    position = models.CharField(max_length=30,choices=(
        ('CENTER', "Left-handed"),
        ('DEFENSEMAN', "Right-handed"),
        ('GOALIE', "Left-handed"),
        ('LEFT_WING', "Left-handed"),
        ('RIGHT_WING', "Left-handed"),
    ))
    points = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    timeouts = models.IntegerField(default=0)

    def get_sport_name(self):
        return "Field_Hockey"

    class Meta:
        unique_together = ('year', 'user')

class Football(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)# get_user_model.obj
    YEAR_CHOICES = (
        ('FRESHMAN YEAR','Freshman Year'),
        ('SOPHMORE YEAR','Sophmore Year'),
        ('JUNIOR YEAR','Junior Year'),
        ('SENIOR YEAR','Senior Year'),
    )
    year = models.CharField(choices=YEAR_CHOICES, default=YEAR_CHOICES[0][0], null=False, max_length=20)
    position = models.CharField(max_length=30,choices=(
        ('CENTER', "Left-handed"),
        ('CORNERBACK', "Right-handed"),
        ('DEFENSIVE_END', "Left-handed"),
        ('DEFENSIVE_TACKLE', "Left-handed"),
        ('DIMEBACK', "Left-handed"),
        ('GUNNER', "Left-handed"),
        ('HOLDER', "Left-handed"),
        ('JAMMER', "Left-handed"),
        ('KICK_RETURNER', "Left-handed"),
        ('KICKER', "Left-handed"),
        ('KICKOFF_RETURNER', "Left-handed"),
        ('LONG_SNAPPER', "Left-handed"),
        ('MIDDLE_LINEBACK', "Left-handed"),
        ('NICKLEBACK', "Left-handed"),
        ('OFFENSIVE_GUARD', "Left-handed"),
        ('OFFENSIVE_TACKLE', "Left-handed"),
        ('PUNTER', "Left-handed"),
        ('RUNNING_BACK', "Left-handed"),
        ('SAFETY', "Left-handed"),
        ('TIGHT_END', "Left-handed"),
        ('UPBACK', "Left-handed"),
        ('WIDE_RECEIVER', "Left-handed"),
    ))
    points = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    timeouts = models.IntegerField(default=0)

    def get_sport_name(self):
        return "Football"

    class Meta:
        unique_together = ('year', 'user')

class Golf(models.Model):
    pass

class Gymnastics(models.Model):
    pass

class Ice_Hockey(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)# get_user_model.obj
    YEAR_CHOICES = (
        ('FRESHMAN YEAR','Freshman Year'),
        ('SOPHMORE YEAR','Sophmore Year'),
        ('JUNIOR YEAR','Junior Year'),
        ('SENIOR YEAR','Senior Year'),
    )
    year = models.CharField(choices=YEAR_CHOICES, default=YEAR_CHOICES[0][0], null=False, max_length=20)
    position = models.CharField(max_length=30,choices=(
        ('CENTER', "Left-handed"),
        ('GOALIE', "Right-handed"),
        ('LEFT_DEFENDER', "Right-handed"),
        ('LEFT_WING', "Right-handed"),
        ('RIGHT_DEFENDER', "Right-handed"),
        ('RIGHT_WING', "Right-handed"),
    ))
    points = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    timeouts = models.IntegerField(default=0)

    def get_sport_name(self):
        return "Ice_Hockey"

    class Meta:
        unique_together = ('year', 'user')

class Soccer(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    YEAR_CHOICES = (
        ('FRESHMAN YEAR','Freshman Year'),
        ('SOPHMORE YEAR','Sophmore Year'),
        ('JUNIOR YEAR','Junior Year'),
        ('SENIOR YEAR','Senior Year'),
    )
    year = models.CharField(choices=YEAR_CHOICES, default=YEAR_CHOICES[0][0], null=False, max_length=20)
    position = models.CharField(max_length=100,choices=(
        ('ATTACKING_MIDFIELDER', "Attacking Midfielder"),
        ('CENTER_BACK', "Center Back"),
        ('CENTER_FORWARD', "Center Forward"),
        ('CENTER_MIDFIELDER', "Center Midfielder"),
        ('DEFENSIVE_MIDFIELDER', "Defensive Midfielder"),
        ('FULLBACK', "Fullback"),
        ('GOALKEEPER', "Goalkeeper"),
        ('LEFT_MIDFIELDER', "Left Midfielder"),
        ('RIGHT_MIDFIELDER', "Right Midfielder"),
        ('SECOND_STRIKER', "Second Striker"),
        ('SWEEPER', "Sweeper"),
        ('STRIKER', "Striker"),
        ('WINGER', "Winger"),
    ))
    points = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    timeouts = models.IntegerField(default=0)

    def get_sport_name(self):
        return "Soccer"

    class Meta:
        unique_together = ('year', 'user')

class Softball(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)# get_user_model.obj
    YEAR_CHOICES = (
        ('FRESHMAN YEAR','Freshman Year'),
        ('SOPHMORE YEAR','Sophmore Year'),
        ('JUNIOR YEAR','Junior Year'),
        ('SENIOR YEAR','Senior Year'),
    )
    year = models.CharField(choices=YEAR_CHOICES, default=YEAR_CHOICES[0][0], null=False, max_length=20)
    position = models.CharField(max_length=30,choices=(
        ('BATTER', "Left-handed"),
        ('CATCHER', "Right-handed"),
        ('FIRST_BASEMAN', "Stopper"),
        ('OUTFIELDER', "Stopper"),
        ('PITCHER', "Stopper"),
        ('SECOND_BASEMAN', "Stopper"),
        ('SHORTSTOP', "Stopper"),
        ('THIRD_BASEMAN', "Stopper"),
    ))
    points = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    timeouts = models.IntegerField(default=0)

    def get_sport_name(self):
        return "Softball"

    class Meta:
        unique_together = ('year', 'user')

class Swimming(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)# get_user_model.obj
    YEAR_CHOICES = (
        ('FRESHMAN YEAR','Freshman Year'),
        ('SOPHMORE YEAR','Sophmore Year'),
        ('JUNIOR YEAR','Junior Year'),
        ('SENIOR YEAR','Senior Year'),
    )
    year = models.CharField(choices=YEAR_CHOICES, default=YEAR_CHOICES[0][0], null=False, max_length=20)
    # Also display number of games per stroke
    freestyle_50 = models.IntegerField(default=0)
    backstroke_100 = models.IntegerField(default=0)
    breaststroke_100 = models.IntegerField(default=0)
    butterfly_100 = models.IntegerField(default=0)
    freestyle_100 = models.IntegerField(default=0)
    free_relay_200 = models.IntegerField(default=0)
    freestyle_200 = models.IntegerField(default=0)
    individual_medley_200 = models.IntegerField(default=0)
    free_relay_400 = models.IntegerField(default=0)
    freestyle_500 = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def get_sport_name(self):
        return "Swimming"

    class Meta:
        unique_together = ('year', 'user')

class Tennis(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)# get_user_model.obj
    YEAR_CHOICES = (
        ('FRESHMAN YEAR','Freshman Year'),
        ('SOPHMORE YEAR','Sophmore Year'),
        ('JUNIOR YEAR','Junior Year'),
        ('SENIOR YEAR','Senior Year'),
    )
    year = models.CharField(choices=YEAR_CHOICES, default=YEAR_CHOICES[0][0], null=False, max_length=20)
    games_won = models.IntegerField(default=0)

    def get_sport_name(self):
        return "Tennis"

    class Meta:
        unique_together = ('year', 'user')

# By default, we want to generate a form that asks how many meteres you run and display their choice.
# To the right of those choices, ask if they do any jumping or throwing in relation to track and field.
class Track_And_Field(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)# get_user_model.obj
    YEAR_CHOICES = (
        ('FRESHMAN YEAR','Freshman Year'),
        ('SOPHMORE YEAR','Sophmore Year'),
        ('JUNIOR YEAR','Junior Year'),
        ('SENIOR YEAR','Senior Year'),
    )
    year = models.CharField(choices=YEAR_CHOICES, default=YEAR_CHOICES[0][0], null=False, max_length=20)
    # Running
    sprint_100_games = models.IntegerField(default=0)
    sprint_100_average = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    sprint_200_games = models.IntegerField(default=0)
    sprint_200_average = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    sprint_400_games = models.IntegerField(default=0)
    sprint_400_average = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    hurdles_100_games = models.IntegerField(default=0)
    hurdles_100_average = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    hurdles_110_games = models.IntegerField(default=0)
    hurdles_110_average = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    hurdles_400_games = models.IntegerField(default=0)
    hurdles_400_average = models.DecimalField(max_digits=7, decimal_places=3, default=0)
    middle_distance_800_games = models.IntegerField(default=0)
    middle_distance_800_average = models.DecimalField(max_digits=7, decimal_places=3, default=0)
    middle_distance_1500_games = models.IntegerField(default=0)
    middle_distance_1500_average = models.DecimalField(max_digits=7, decimal_places=3, default=0)
    long_distance_3000_games = models.IntegerField(default=0)
    long_distance_3000_average = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    long_distance_5000_games = models.IntegerField(default=0)
    long_distance_5000_average = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    long_distance_10000_games = models.IntegerField(default=0)
    long_distance_10000_average = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    # Jumping BEST TIME

    def get_sport_name(self):
        return "Track_And_Field"

    class Meta:
        unique_together = ('year', 'user')

class Volleyball(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)# get_user_model.obj
    YEAR_CHOICES = (
        ('FRESHMAN YEAR','Freshman Year'),
        ('SOPHMORE YEAR','Sophmore Year'),
        ('JUNIOR YEAR','Junior Year'),
        ('SENIOR YEAR','Senior Year'),
    )
    year = models.CharField(choices=YEAR_CHOICES, default=YEAR_CHOICES[0][0], null=False, max_length=20)
    position = models.CharField(max_length=30,choices=(
        ('LEFT_HANDED', "Left-handed"),
        ('RIGHT_HANDED', "Right-handed"),
    ))
    points = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    timeouts = models.IntegerField(default=0)

    def get_sport_name(self):
        return "Volleyball"

    class Meta:
        unique_together = ('year', 'user')


class Wrestling(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)# get_user_model.obj
    YEAR_CHOICES = (
        ('FRESHMAN YEAR','Freshman Year'),
        ('SOPHMORE YEAR','Sophmore Year'),
        ('JUNIOR YEAR','Junior Year'),
        ('SENIOR YEAR','Senior Year'),
    )
    year = models.CharField(choices=YEAR_CHOICES, default=YEAR_CHOICES[0][0], null=False, max_length=20)
    position = models.CharField(max_length=30,choices=(
        ('LEFT_HANDED', "Left-handed"),
        ('RIGHT_HANDED', "Right-handed"),
    ))
    points = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    timeouts = models.IntegerField(default=0)

    def get_sport_name(self):
        return "Wrestling"

    class Meta:
        unique_together = ('year', 'user')
