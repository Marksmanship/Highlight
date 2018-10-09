from django.conf.urls import url
from . import views

app_name = 'Posts_Namespace'
urlpatterns = [
	url(r'^$', views.Post_List, name="Posts_List"),
	url(r'^(?P<id>\d+)/$', views.Post_Detail, name="Posts_Detail"), # {% url "Post_Detail" id=obj.id %}
	url(r'^create$', views.Post_Create, name="Posts_Create"),
	url(r'^update$', views.Post_Update, name="Posts_Update"),
	url(r'^delete$', views.Post_Delete, name="Posts_Delete"),
]
