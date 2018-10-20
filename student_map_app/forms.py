from django.forms import ModelForm
from django import forms


class SchoolSearchForm(forms.form):
	school_search = forms.CharField(max_length=100, min_length=10)

class SchoolSelectForm(ModelForm):
		school_options = forms.ChoiceField(choices = [])
	Class Meta:
		model = User_School
		fields = ['school_options']
