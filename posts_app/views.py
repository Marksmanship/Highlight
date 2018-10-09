from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.

def Post_List(request):
	template_name = 'Blog.html'
	queryset = Post.objects.all()
	context = {
		"post_objects": queryset,
	}

	return render(request, template_name, context )

def Post_Detail(request, id=None):
	template_name = "Post_Detail.html"
	instance = get_object_or_404(Post, id=id)
	context = {
		"instance": instance,
	}
	return render(request, template_name, context)
	# context = postobject.get(id)

def Post_Create(request):
	pass

def Post_Update(request):
	pass

def Post_Delete(request):
	pass
