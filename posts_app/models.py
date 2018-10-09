from django.db import models

# Create your models here.
DEFAULT_BLOG = "defaults/default_blog.png"
class Post(models.Model):
	title = models.CharField(max_length=120)
	thumbnail = models.ImageField(blank=False, null=False, default=DEFAULT_BLOG)
	#slug = models.SlugField()
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)	# Auto_Now_Add = True -- When the post is first made, populates this field
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)	# Auto_Now = True -- When the post is updated, update this field

	def delete_image(self):
		self.image.delete(save=False)
		self.image = DEFAULT-IMAGE
		self.save()
	def get_object_or_404(self):
		return "/blog/%s" % (self.id)
	def __str__(self):
		return self.title
