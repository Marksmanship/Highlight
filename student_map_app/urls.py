from django.conf.urls import url
from . import views

app_name = "Student_Maps_Namespace"
# Handles domain/account/school
urlpatterns = [
    url(r'^$', views.SchoolLanding, name="School_Landing_View"),
    url(r'^search/$', views.SchoolSearch, name="School_Search_View"),
    url(r'^select/$', views.SchoolSelect, name="School_Select_View"),
]
