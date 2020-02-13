from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save, pre_delete, post_delete

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


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

	def get_user_type(self):
		return self.occupation
	def __str__(self):
		return "%s %s" % (self.first_name, self.last_name)

class UserProfile(models.Model):
	DEFAULT_AVATAR = 'defaults/default_avatar.jpg'
	DEFAULT_BANNER = 'defaults/default_banner.png'

	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	phone = models.IntegerField(default=0, null=True, blank=True)
	avatar = models.ImageField(upload_to='user_avatar', blank=True, null=True, default=DEFAULT_AVATAR)	# blank=true means the field is not required for validation
	banner = models.ImageField(upload_to='user_banner', blank=True, null=True, default=DEFAULT_BANNER) # null=true allows null values in database

	def set_default_avatar(self):
		self.avatar.delete(save=False)
		self.avatar = DEFAULT_AVATAR
		self.save()

	def __str__(self):
		return "%s" % (self.user.username)	# access the user field, which links the User table, to grab the username

class Friend(models.Model):
	users = models.ManyToManyField(settings.AUTH_USER_MODEL)
	current_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="owner", null=True, on_delete=models.CASCADE)

	@classmethod
	def make_friend(cls, initiator, new_friend):
		friend, created_friend = cls.objects.get_or_create(current_user=initiator) # Tuple unpacking. Ensure there is only one row per initiator in friend table
		friend.users.add(new_friend)
	@classmethod
	def remove_friend(cls, initiator, new_friend):
		friend, created_friend = cls.objects.get_or_create(current_user=initiator) # Ensure there is only one row per initiator in friend table
		friend.users.remove(new_friend)

class Gallery(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="gallery_images", blank=True)
	uploaded = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		if self.image:
			return "%s uploaded %s" % (self.user.username, self.image.url)
		return '%s' % self.user.first_name

class Activity(models.Model):
	ACTIVITY_CHOICES = (
		('F', 'Favorite'),
		('L', 'Like'),
		('U', 'Upload')
	)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	activity_choice = models.CharField(max_length=1, choices=ACTIVITY_CHOICES)
	activated = models.BooleanField()
	timestamp = models.DateTimeField(auto_now=True)

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

# These don't work if done from phpmyadmin
# The post_save signal comes with the kwargs: created (bool), instance (object and its fields), and sender (model class)
def create_profile(sender, **kwargs): # All signal handlers must have at least these two parameters, even if kwargs is empty.
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])
		user_profile.save()
def create_gallery_activity(sender, **kwargs):
	if kwargs['created']:
		content_type = ContentType.objects.get_for_model(Gallery)
		user_activity = Activity.objects.create(user=kwargs['instance'].user, content_type=content_type, object_id=int(kwargs['instance'].id), activity_choice="U", activated=True)
		user_activity.save()
def delete_gallery_activity(sender, **kwargs):
	print("deleting")
	content_type = ContentType.objects.get_for_model(Gallery)
	user_activity = Activity.objects.get(object_id=kwargs['instance'].id, content_type=content_type)
	user_activity.delete()
post_save.connect(create_gallery_activity, sender=Gallery)
post_save.connect(create_profile, sender=User)
# post_delete.connect(delete_gallery_activity, sender=Gallery)
