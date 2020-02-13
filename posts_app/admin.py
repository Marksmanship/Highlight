from django.contrib import admin
from .models import Post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "is_published", "created", "updated"] # Display the field(s) __
	list_filter = ('is_published',)	# Can filter by __
	search_field = ('title',)	# Search bar looks through __
	exclude = ('slug',)

admin.site.register(Post, PostModelAdmin)
