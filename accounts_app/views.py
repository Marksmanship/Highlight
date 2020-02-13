from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.forms.models import inlineformset_factory
from django.db.models import Q

from .forms import RegistrationForm, ProfileEditForm, GalleryForm
from .models import Gallery, User, UserProfile, Friend
from athlete_and_school_app.models import User_Sport
from student_map_app.models import *
from posts_app.models import Activity

import json

def Register(request):
	form_class = RegistrationForm
	template_name = 'dashboard_app/Home.html'

	if request.method == 'POST':
		form = form_class(request.POST)
		username = request.POST.get('username') # This is the "name" attribute of the input field generated automagically
		password = request.POST.get('password1') # This is the "name" attribute of the input field generated automagically. User instance's password is set to password1 within the RegistrationForm per documentation

		if form.is_valid():
			form.save()
			user = authenticate(username=username, password=password)
			if user is not None:
				print("SHOULDA WORKED")
				login(request, user)
				return redirect('/account/profile/')
	else:
		form = form_class()

	return render(request, template_name, {'form': form})

def ChangePassword(request):
	pass

def Login(request):
	username = request.POST.get('login-username')	# if you can find a value, return an empty string
	password = request.POST.get('login-password')
	user = authenticate(username=username, password=password) # Ensuring that this user exists

	if user is not None:
		login(request, user)
		return redirect('/account/profile/')
	else:
		return redirect('/')

def Logout(request):
	if request.method == 'GET':
		logout(request)
	return redirect('/')

def AlterFriend(request, operation, slug):
	# Both operation and slug are determined by manual input into URL
	new_friend = User.objects.get(username=slug)
	if operation == "add":
		Friend.make_friend(request.user, new_friend)
	elif operation == "remove":
		Friend.remove_friend(request.user, new_friend)
	else:
		pass
	return redirect("/account/profile/")

def ViewProfile(request, slug=None):
	if request.method == "GET":
		# Handle viewing others' profiles
		if slug:
			pageOwner = User.objects.get(username=slug)
		else:
			pageOwner = request.user

		# Get current user's friends
		friends = Friend.objects.get(current_user=request.user).users.all()

		# User avatar and banner
		userProfile = UserProfile.objects.get(user=pageOwner)

		# Suggestions
		suggestedAthletes = User.objects.filter(~Q(id=request.user.id), Q(is_staff=0), Q(occupation="A"))[0:5]
		suggestedCoaches = User.objects.filter(~Q(id=request.user.id), Q(is_staff=0))

		# Generate Sport Tables of Page Owner
		userSportList = User_Sport.objects.filter(student_id=pageOwner)
		sportArray = []
		for sport in userSportList:
			sportName = sport.get_sport_name()
			sportArray.append(eval('%s.objects.filter(user=request.user)' % sportName))

		# Render relevant Page Owner activity
		activityArray = []
		activityObjects = Activity.objects.filter(user_id=pageOwner.id).order_by("-timestamp")
		for object in activityObjects:
			tempString = None
			if object.activated:
				if object.activity_choice=="L":
					tempString = "%s liked an <a href='/blog/%s'>article</a> by %s on %s." % (object.user.username, object.content_object.slug, object.user, object.timestamp)
				elif object.activity_choice=="U":
					tempString = "%s uploaded an image to the gallery on %s" % (object.user.username, object.timestamp)
				activityArray.append(tempString)

		# Display Page Owner gallery
		galleryArray = Gallery.objects.filter(user=pageOwner).order_by('uploaded')

	args = {
	'Sport_Objects': sportArray,
	'Gallery_Objects': galleryArray,
	'Activity_Objects': activityArray,
	"User_Profile": userProfile,
	"Page_Owner": pageOwner,
	"Suggested_Athletes": suggestedAthletes,
	"Friends": friends,}
	return render(request, 'accounts_app/Profile.html', args)


def EditProfile(request):
	user = User.objects.get(username=request.user.username)
	userGallery = Gallery.objects.filter(user=user)

	# Generate formset. Forms take initial data as a dictionary. Formsets take an array of dictionaries
	galleryInlineFormSet = inlineformset_factory(get_user_model(), Gallery, form=GalleryForm, extra=5) # We didn't have to specify a custom form, but we did just in case we want to change the widget
	userGalleryInitial = [{'image': instance.image, 'image_url':instance.image.url} for instance in userGallery if instance.image]

	if request.method == "POST":

		# Bind the profileeditform because we'll be hosting this gallery image form on the same page.
		profile_form = ProfileEditForm(request.POST, instance=user)

		# Bind the formset with POST and Initial data. The instance argument prevents us from getting a save() prohibited error.
		gallery_inlineformset = galleryInlineFormSet(request.POST, request.FILES, instance=user, initial=userGalleryInitial, prefix="gallery")

		# After we get the id POSTed from Edit_Profile.js, we want to grab the image element of index: indx and set
		# Once we grab the id, we must
		if request.is_ajax():
			galArray = Gallery.objects.filter(user=user)
			galArray[int(request.POST.get('imageNumber'))].delete()

			response2 = {'success': "YOOO NIGGA"}
			return HttpResponse(json.dumps(response2))

		if profile_form.is_valid() and gallery_inlineformset.is_valid():
			# Altering the User model with data POSTed from the UserProfile. We don't have the profile on the Edit page yet.
			user.first_name = profile_form.cleaned_data['first_name']
			user.last_name = profile_form.cleaned_data['last_name']
			user.save()

			# Handle saving of new and updated images
			for form in gallery_inlineformset: # Contains all forms in the set whether empty or pre-populated
				if ('image' in form.changed_data):	# If the current form's image has changed...
					if form.initial.get('image') is not None:	# If there was no image before the post, request, just save the form. Otherwise, compare initial data
						myObject = Gallery.objects.get(user=user, image=form.initial['image'])
						myObject.image = form.cleaned_data.get('image')
						myObject.save()
					else:
						form.save()
	else:
		# Get the profile details of the logged-in user; display user's gallery
		profile_form = ProfileEditForm(user)
		gallery_inlineformset = galleryInlineFormSet(initial=userGalleryInitial, prefix="gallery")
		print("USER GALLERY: " + str(userGallery))
		print("GALLERY INITIAL: " + str(userGalleryInitial))
	args = {'Gallery_Inlineformset': gallery_inlineformset }
	return render(request, 'accounts_app/Edit_Profile.html', args)
