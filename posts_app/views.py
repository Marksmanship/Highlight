from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def Post_List(request):
	template_name = 'dashboard_app/Blog.html'
	Posts = Post.objects.all()

	paginator = Paginator(Posts, 3)
	page = request.GET.get('page')
	paged_listings = paginator.get_page(page)

	context = {
		"post_objects": paged_listings,
	}
	return render(request, template_name, context)

def Post_Detail(request, pk=None):				 # The 'pk=none' makes the pk argument optional
	template_name = "dashboard_app/Post_Detail.html"
	post_object = get_object_or_404(Post, id=pk) # Setting the Post ID equal to the id passed by the URL. ID is gathered from a method defined withint the model
	context = {
	 	"post_objects": post_object,
	 }
	return render(request, template_name, context)

def Post_Create(request):
	pass

def Post_Update(request):
	pass

def Post_Delete(request):
	pass
