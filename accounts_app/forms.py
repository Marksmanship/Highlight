from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm	# Django pre-populated form that accepts a meta model
from django.contrib.auth import get_user_model			# Import our customized user model
from .models import UserProfile

# Declare our custom User model
CustomUser = get_user_model()

# RegistrationForm inherits UserCreationForm which contains the Username, Password1, Password2 fields
# UserCreationForm inherits ModelForm and its Meta() inherits the User Model (table), so it makes records on the User table on each save
class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=70, required=True)
	class Meta:
		# Also populate this form with User Model )
		model = CustomUser
			# first_name,
			# last_name,
			# password,
			# username,
			# email,
			# occupation
		# Fields that the RegistrationForm will display
		fields = [
			'first_name',
			'last_name',
			'email',
			'occupation',
			'username',
			'password1',
			'password2'
		]
	# Reserved constructor
	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs={ 'class': 'Form-Half', 'id': 'registry-first-name', 'placeholder': 'Enter first name'}
		self.fields['last_name'].widget.attrs={ 'class': 'Form-Half', 'id': 'registry-last-name', 'placeholder': 'Enter last name'}
		self.fields['username'].widget.attrs={ 'class': 'Form-Half', 'id': 'registry-username', 'placeholder': 'Enter username'}
		self.fields['occupation'].widget.attrs={ 'class': 'Form-Half', 'id': 'registry-occupation'}
		self.fields['password1'].widget.attrs={ 'class': 'Form-Half', 'id': 'registry-password1', 'placeholder': 'Enter password'}
		self.fields['password2'].widget.attrs={ 'class': 'Form-Half', 'id': 'registry-password2', 'placeholder': 'Re-enter password'}
		self.fields['email'].widget.attrs={ 'class': 'Form-Full', 'id': 'registry-email', 'placeholder': 'Enter email address'}

	# Some form validation
	def save(self, commit=True):
		# Use "self's" (RegistrationForm's) class definition of "save"
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		if commit:
			user.save()

class ProfileEditForm(UserChangeForm):

	class Meta:
		model = CustomUser
		fields = [
			'email',
			'first_name',
			'last_name'
		]
