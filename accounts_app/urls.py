from django.conf.urls import url
from .import views

app_name = 'Accounts_Namespace'
urlpatterns = [
	url(r'^$', views.Register, name='Accounts_Register'),					# Register on home_page
	url(r'^change-password/$', views.ChangePassword, name="Accounts_Change_Password"),
	url(r'^login/$', views.Login, name='Accounts_Login'),
	url(r'^logout/$', views.Logout, name='Accounts_Logout'),
	url(r'^profile/$', views.ViewProfile, name='Accounts_View_Profile'),
	url(r'^profile/edit/$', views.EditProfile, name="Accounts_Edit_Profile"),

]
