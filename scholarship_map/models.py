from django.db import models, connection
from django.conf import settings

# One-To-Many only works in one direction in django, that direction being Many-To-One. This means
# that you must set the foreign key constraints on the many side. ForeignKey is only one-to-one
# if you specify ForeignKey(unique=True).Add FK to the one side.
# SCHOOLS:
# --------
class School(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    school_name = models.CharField(max_length=100, null=False, blank=False)
    school_address = models.CharField(max_length=100, blank=True, null=True) # Can be left as an empty string in DB

    class Meta:
		# db_table = "Database_Schools"
        verbose_name = 'School'
        verbose_name_plural = 'Schools'
    def __str__(self):
        return '%s, %s' % (self.id, self.school_name)

# SPORTS:
# -------
class Sport(models.Model):
    SPORTS_CHOICES = (
        (1, ('Baseball')),
		(2, ('Basketball')),
		(3, ('Bowling')),
		(4, ('Cheerleading')),
		(5, ('Cross Country')),
		(6, ('Dance Team')),
		(7, ('Football')),
		(8, ('Golf')),
		(9, ('Gymnastics')),
		(10, ('Hockey')),
		(11, ('Soccer')),
		(12, ('Softball')),
		(13, ('Swimming')),
		(14, ('Tennis')),
		(15, ('Track & Field')),
		(16, ('Volleyball')),
		(17, ('Wrestling'))
    )
    sports_id = models.AutoField(primary_key=True, null=False)		# Number correlating to sport name
    sports_name = models.IntegerField(choices=SPORTS_CHOICES, default=1, null=False, unique=True)

    class Meta:
        verbose_name = "Sport"
        verbose_name_plural = "Sports"

    def __str__(self):
        return '%s' % (self.sports_name)

# SCHOOL-SPORTS: [Many-To-One with 'Schools' (One school can have many sports) | Many-To-One with 'Sports' (One sport, many schools)]
# Basically, each instancce of School_Sport will have access to one school and one sport. We enforce that each instance must contains
# a unique combination of school and sport, as a user will only be allowed to associate with one sport in a school.
# --------------
class School_Sport(models.Model):
    unique_id = models.AutoField(primary_key=True) 	#Can't set school to primary key, because the school's id  alone would be unique
    ss_school_id = models.ForeignKey('School', related_name='ss_school_id', on_delete=models.CASCADE) # instances of School_Sport will have access to one unique school. See Meta
    ss_sports_id = models.ForeignKey('Sport', related_name="ss_sports_id", on_delete=models.CASCADE) # Sport has access to School_Sport instance through school_sport_set.all()

    class Meta:
        # Composite key
        # School 1 can appear multiple times in this one-to-many relationship
        # but cannot be coupled with the same sport more than once
        unique_together = ('ss_school_id', 'ss_sports_id')
        verbose_name = "School_Sport"
        verbose_name_plural = "School_Sports"
    def my_custom_sql(self):
        cursor = connection.cursor()
        cursor.execute("SELECT school_name FROM scholarship_map_school where id=%s", [self.ss_school_id])
        raw_name = cursor.fetchall()
        return raw_name
    def __str__(self):
        return '[%s] has [%s]' % (self.my_custom_sql(), self.ss_sports_id)
# USER-SCHOOLS: [Many-To-One with 'Users' (One user many school scholarships) | Many-To-One with 'Schools' (One school many users)]
# -------------
class User_School(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_school_set', on_delete=models.CASCADE)		# Populate by grabbing request.user from form
    school_id = models.ForeignKey('School_Sport', on_delete=models.CASCADE) # Decide which related name you want to use for this model

    class Meta:
        unique_together = ('student_id', 'school_id')
        verbose_name = "User_School"
        verbose_name_plural = "User_Schools"

# USER-SPORTS: [Many-To-One with 'Users' (One user multiple sports) | Many-To-One with 'Sports' (One sport multiple users)]
# ------------
class User_Sport(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='usersports_student_id', on_delete=models.CASCADE)
    sports_id = models.ForeignKey('Sport', related_name='usersports_sports_id', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('student_id', 'sports_id')
        verbose_name = "User_Sport"
        verbose_name_plural = "User_Sports"

    def __str__(self):
        return '[%s] plays [%s]' % (self.student_id, self.sports_id)

# SPORT STATS - USERS:
# --------------------
class Sport_Stat(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, related_name='my_user', on_delete=models.CASCADE)
    position = models.CharField(max_length=40, null=False)
    matches_won = models.IntegerField(default=0, null=False)

    class Meta:
        verbose_name = "Sport_Stat"
        verbose_name_plural = "Sports_Stats"
