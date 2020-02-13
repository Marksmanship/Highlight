from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from accounts_app.models import Activity
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import get_user_model

from django.contrib.contenttypes.models import ContentType
import json
from django.http import HttpResponse
# Create your views here.

def Post_List(request):
	template_name = 'posts_app/Post_List.html'
	Posts = Post.objects.order_by('created').filter(is_published=True)

	paginator = Paginator(Posts, 6)
	page = request.GET.get('page') # The page we're on
	paged_listings = paginator.get_page(page) # Paginated list

	context = {
		"Post_Page": paged_listings,
	}
	return render(request, template_name, context)

# Slug taken from URL input
def Post_Detail(request, slug=None):
	template_name = "posts_app/Post_Detail.html"
	postObject = get_object_or_404(Post, slug=slug) # Setting the Post ID equal to the id passed by the URL. ID is gathered from a method defined withint the model
	likeStatus = None



	# If there is a Post object in the activity table where the id of the post equals the id of the
	# post captured by the slug, mark it as a pre-existing object.
	preExistingObject = None
	if (Activity.objects.filter(activity_choice="L", post_likes_rn__id=postObject.id)):
	    preExistingObject = Activity.objects.get(activity_choice="L", post_likes_rn__id=postObject.id)

	# If there is a pre-existing object, set a cookie within the response indicating whether it's
	# liked or not.
	if preExistingObject:
		if preExistingObject.activated:
			likeStatus = "Liked"
		else:
			likeStatus = "Disliked"
	args = { "Post_Object": postObject, "Like_Status": likeStatus}
	return render(request, template_name, args)


def like(request):
	user = request.user
	likeStatus = None
	if request.method == 'POST':
		print(request.POST.get('objectId'))
		# In PostDetail view, we grab the post id by filtering with the slug inputted into the URL.
		# This enables us to show any post associated with that URL. When the user clicks the like
		# button, that id is grabbed from within the template via inline javascript, and an external js
		# file uses ajax to POST that id variable to this view. We use the id for the content_object field.
		objectId = request.POST.get('objectId')
		contentObject = Post.objects.get(pk=objectId)



		# If the post object we've just liked already exists, put it in the preExistingObject variable
		# otherwise create the object.
		# From the Activity table, get all Post objects where the id of the post is equal to the id of
		# the blog being read (the blog itself is posted from the blog's page)
		preExistingObject = None
		likedObject = None
		if (Activity.objects.filter(activity_choice="L", post_likes_rn__id=objectId)):
			preExistingObject = Activity.objects.get(activity_choice="L", post_likes_rn__id=objectId, user=user.id)
		else:
			likedObject = Activity.objects.create(user=user, content_object=contentObject, activity_choice="L", activated=True)

		# If the blog POSTed to us was activated, deactivate it (set to Not-Liked) and vice-versa
		if preExistingObject:
			if preExistingObject.activated:
				preExistingObject.activated = False
				preExistingObject.save()
				likeStatus = 'Disliked'
			elif preExistingObject.activated == False:
				preExistingObject.activated = True
				preExistingObject.save()
				likeStatus = 'Liked'
		elif likedObject:
			likedObject.save()
			likeStatus = 'Never-Liked'
		else:
			print("ERROR: Object is neither prexisting or new.")

		response = {'Like_Status': likeStatus}
	return HttpResponse(json.dumps(response), content_type="application/json")

def Post_Create(request):
	pass

def Post_Update(request):
	pass

def Post_Delete(request):
	pass
