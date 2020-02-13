from django.conf.urls import url
from . import views

app_name = 'Student_Maps_Namespace'
# Handles domain/account/affiliations/
urlpatterns = [
    url(r'^$', views.SchoolLanding, name="School_Landing_View"),
    url(r'^school/$', views.SchoolSelect, name="School_Search_View"),
    url(r'^sport/$', views.SchoolSportSelect, name="School_Sport_View"),
    url(r'^sport/edit/$', views.SchoolSportEdit, name="School_Sport_Fill_View"),
]
