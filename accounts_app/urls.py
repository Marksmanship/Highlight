from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
app_name = 'Accounts_Namespace'
# Handles Domain/account
urlpatterns = [
	url(r'^$', views.Register, name='Accounts_Register'),					# Register on home_page
	url(r'^change-password/$', views.ChangePassword, name="Accounts_Change_Password"),
	url(r'^connect/(?P<operation>.+)/(?P<slug>[-\w]+)/$', views.AlterFriend, name="Accounts_Alter_Friend"),
	url(r'^login/$', views.Login, name='Accounts_Login'),
	url(r'^logout/$', views.Logout, name='Accounts_Logout'),
	url(r'^profile/$', views.ViewProfile, name='Accounts_View_Profile'),
	url(r'^profile/(?P<slug>[-\w]+)/$', views.ViewProfile, name='Accounts_View_Profile_Other'),
	url(r'^edit/$', views.EditProfile, name="Accounts_Edit_Profile"),
	url(r'^affiliations/', include('student_map_app.urls', namespace='Student_Maps_Namespace')),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += patterns('',
#         (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#         'document_root': settings.MEDIA_ROOT}))
