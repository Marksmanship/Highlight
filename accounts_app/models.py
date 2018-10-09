from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.conf import settings

class User(AbstractUser):
	OCCUPATIONS = (
		('A','Athlete'),
		('C','Coach'),
		('P','Parent'),
	)

	# first_name
	# last_name
	# password
	# username
	# email
	occupation = models.CharField(default='A', max_length=30,choices=OCCUPATIONS)

class UserProfile(models.Model):
	DEFAULT_AVATAR = 'defaults/default_avatar.jpg'
	DEFAULT_BANNER = 'defaults/default_banner.png'

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	city = models.CharField(max_length=100, null=True, blank=True)
	phone = models.IntegerField(default=0, null=True, blank=True)
	avatar = models.ImageField(upload_to='user_avatar', blank=True, null=True, default=DEFAULT_AVATAR)	# blank=true means the field is not required for validation
	banner = models.ImageField(upload_to='user_banner', blank=True, null=True, default=DEFAULT_BANNER) # null=true allows 'None' to be used in Python code and registers as null in database

	def set_default_avatar(self):
		self.avatar.delete(save=False)
		self.avatar = DEFAULT
		self.save()

	def __str__(self):
		return "%s" % (self.user.username)

# Function to invoke once we connect to a save() of User
def create_profile(sender, **kwargs):
	# Django's post_save method sends a 'created' boolean argument (if a new record was created)
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])
		user_profile.save()
# Once an instance of User is saved, call create_profile()
post_save.connect(create_profile, sender=User)


# class Gallery(models.Model):
# 	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
# 	image = models.ImageField(upload_to='user_gallery', blank=True, null=True, verbose_name="")
# 	# Foreign key field rendered as user_id. This field is by default, excluded from forms
#
# 	def __str__(self):
# 		return "%s" % (self.user)
# # Function to invoke once we connect to a save() of User
# def create_gallery(sender, **kwargs):
# 	if kwargs['created']:
# 		user_gallery = Gallery.objects.create(user=kwargs['instance'])
# 		user_gallery.save();
# post_save.connect(create_gallery, sender=User)
# @receiver(post_save, sender=User)
# def create_gallery(sender, instance, created, **kwargs):
# 	if created:
# 		Gallery.objects.create(user=instance)
	# @receiver(post_save, sender=User)
	# def save_gallery(sender, instance, **kwargs):
	# 	instance.gallery.save()
