from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from .forms import RegistrationForm, ProfileEditForm

def Register(request):
	form_class = RegistrationForm
	template_name = 'dashboard_app/Home.html'

	# if request.method == 'POST':
	# 	form = form_class(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	#
	# 		username = form.cleaned_data['username']
	# 		password = form.cleaned_data['password1']
	# 		user = authenticate(username=username, password=password)
	#
	# 		if user is not None:
	# 			if user.is_active:
	# 		 		login(request, user)
	# 		 		return redirect('profile/')
	# else:
	# 	form = form_class()
	# 	return render(request, template_name, {'form': form})

def ChangePassword(request):
	pass

def Login(request):
	username = request.POST['login-username']	# if you can find a value, return an empty string
	password = request.POST['login-password']
	user = authenticate(username=username, password=password)

	if user is not None:
		login(request, user)
		return redirect('/account/profile/')
	else:
		return redirect('/')

def Logout(request):
	if request.method == 'POST':
		logout(request)
	return redirect('/')

def ViewProfile(request):
	return render(request, 'accounts_app/profile.html', {'user': request.user})

# Trying to display the image upload field on the EditProfile
# and display the actual image on the Profile page
def EditProfile(request):
	if request.method == 'POST':
		form = ProfileEditForm(request.POST, instance=request.user) # A subclass of ModelForm can accept an existing instance to update-- we're updating an instance of the current User (instance = atricle.objects.get(pk=1))

		if form.is_valid():
			form.save()
			return redirect("/account/profile/")
	else:
		form = ProfileEditForm(instance=request.user)
		args = {'form': form}
		return render(request, 'accounts_app/editprofile.html', {'form': form})
