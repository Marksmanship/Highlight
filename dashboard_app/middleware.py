import re
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout,login,authenticate
from django.urls import reverse
from accounts_app.forms import RegistrationForm, ProfileEditForm


# If a list by this name exists in settings...
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
	# Loop through it, and recreate this list in a variable located in this file
	# Exempt urls are urls that you don't have to be logged in to access
	EXEMPT_URLS = [(re.compile(url.lstrip('/') ))for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequriedMiddleware:
	# By default, __init__ is passed info identifying the Sender and instance of a created model.
	# Since this isn't a model, we will have to pass it a request to identify the Sender.
	# Here, we are overwriting the __init__() and defining a parameter to reference the aforementioned info passed by default
	# Then, we are setting the value for that default info to the parameter variable so that we have a reference to it.
	def __init__(self, get_response):
		self.get_response = get_response


	# __Call__ is used to redefine existing objects (objects already created by __init__()).
	# If you were to use __init__ instead, the system would create a new instance of an existing instance
	# __Init__() is used when the class is called to create an instance, __Call__() is used when an instance is called
	def __call__(self, request):
		response = self.get_response(request)
		return response

	# request: Default parameter made by django
	# view_func: Right before django calls a function defined in a view, the function is taken and passed to this view_func parameter
	def process_view(self, request, view_func, view_args, view_kwargs):
		# If the request object contains a user
		assert hasattr(request, 'user')
		# Defining the path variable to be used in comparison of URLs
		path = request.path_info.lstrip('/')

		# Bool for determining if the page the user is trying to access is one that doesn't require a login
		url_is_exempt = any(pageToBeAccessed.match(path) for pageToBeAccessed in EXEMPT_URLS)

													# Request contains the user object

		# If a logged in user tries to access a page that doesn't require a login
		if request.user.is_authenticated and url_is_exempt:
			# Return them to the page user's are sent to after they log in
			# print("USER IS LOGGED IN BUT URL IS ONLY FOR ANONS")
			return redirect(settings.LOGIN_REDIRECT_URL)
		# If a logged in user tries to acces a page that does require login
		# OR the user is not logged in and the page doesn't require login
		elif request.user.is_authenticated or url_is_exempt:
			# print("USER IS LOGGED IN AND VISITING LOGIN-REQUIRED URLS **OR** THE ANON IS VISITING ANON SITES")
			return None
		# If a user is not logged in and the page requires login(!user.is_authenticated && !url_is_exempt)
		else:
			# print("AN ANON IS TRYING TO ACCESS A LOGIN-REQUIRED PAGE")
			# Return them to the login form
			return redirect(settings.LOGIN_URL)

		# Note, because process_view is called before analyzing the view we've defined, in the case of logout,
		# django see's we're still logged in. Account/logout requires users to be logged in. As seen above in
		# the second conditional, if the user is logged in and the url isn't exempt, they stay on the same page.
		# For this case --where an user is requesting the logout page-- we need an exception.
		if path == reverse('Accounts_Namespace:Accounts_Logout').lstrip('/'):	# Reverse allows us to grab the url correlating to a view. Remove beginning '/' for pattern match below
			print("LOGGING OUT USER FROM MIDDLEWARE")
			logout(request)
