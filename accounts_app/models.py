from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save

class User(AbstractUser):	# Abstract/Auth User used when altering field count of User model
	OCCUPATIONS = (
		('A','Athlete'),
		('C','Coach'),
		('P','Parent'),
	)
	# User: first_name
	# User: last_name
	# User: password
	# User: username
	# User: email
	occupation = models.CharField(default='A', max_length=30,choices=OCCUPATIONS)
	# child = models.ForeignKey('self', blank=True, null=True, default=None, on_delete=models.CASCADE)
class UserProfile(models.Model):
	DEFAULT_AVATAR = 'defaults/default_avatar.jpg'
	DEFAULT_BANNER = 'defaults/default_banner.png'

	user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
	city = models.CharField(max_length=100, null=True, blank=True)
	phone = models.IntegerField(default=0, null=True, blank=True)
	avatar = models.ImageField(upload_to='user_avatar', blank=True, null=True, default=DEFAULT_AVATAR)	# blank=true means the field is not required for validation
	banner = models.ImageField(upload_to='user_banner', blank=True, null=True, default=DEFAULT_BANNER) # null=true allows null values in database

	def set_default_avatar(self):
		self.avatar.delete(save=False)
		self.avatar = DEFAULT_AVATAR
		self.save()

	def __str__(self):
		return "%s" % (self.user.username)	# access the user field, which links the User table, to grab the username

# The logic here: the post_save signal is sent at the end of a save() method. It comes with a boolen named 'created' whose value depends
# on whether or not a new record was created. When someone creates a new user object, a new record is created, thus the boolen is equal to
# true. We created a 'Signal Handler' named 'create_profile' in which logic is defined that assigns creates a new User_Profile and assigns
# it to the user that just had his account created. This is put into action by connecting this signal handler to the post_save method.

def create_profile(sender, **kwargs): # All signal handlers must have at least these two parameters, even if kwargs is empty.
	if kwargs['created']: 			  # Django's post_save method contains a 'created' boolean argument (if a new record was created)
		user_profile = UserProfile.objects.create(user=kwargs['instance']) # 'instance' initially derives from post_init signal, which is created at model instantiation
		user_profile.save()
post_save.connect(create_profile, sender=User)
