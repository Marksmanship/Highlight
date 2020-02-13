from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from accounts_app.models import Activity


class Post(models.Model):
	DEFAULT_BLOG_IMAGE = "defaults/default_blog.png"
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=250)
	body = models.TextField()
	seo_title = models.CharField(max_length=60, blank=True, null=True)
	seo_description = models.CharField(max_length=165, blank=True, null=True)
	thumbnail = models.ImageField(blank=False, null=False, default=DEFAULT_BLOG_IMAGE)
	slug = models.SlugField(max_length=200, unique=True, default=" ")
	is_published = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	likes = GenericRelation(Activity, related_query_name="post_likes_rn")
	class Meta:
		managed = True

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)
	def delete_image(self):
		self.image.delete(save=False)
		self.image = DEFAULT_BLOG_IMAGE
		self.save()
	def get_object_or_404(self): # Utilized by the view
		return "/blog/%s" % (self.id)
	def __str__(self):
		return self.title
