from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "Base_Namespace"	# The application namespace-- give the same name as application
urlpatterns = [
	url(r'^$', views.Home, name="Base_Home_View"),
	url(r'^about/', views.About, name="Base_About_View"),
	url(r'^account/', include('accounts_app.urls', namespace="Accounts_Namespace")), 	# All urls defined in accounts_app.urls are a part of the application namespace of whatever the app_name variable is defined to within that url file. The namespace specified here, should be the same name as the app_name of the url file you're linking to
	url(r'^admin/', admin.site.urls),
	url(r'^blog/', include('posts_app.urls', namespace="Posts_Namespace")),
	url(r'^sports/', views.Sports, name="Base_Sports_View"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
