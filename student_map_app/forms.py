from django import forms
from django.forms import ModelForm
from athlete_and_school_app.models import Sport
from student_map_app.models import *

class SchoolSearchForm(forms.Form):
	# Name the search box. Input field can be Textarea or TextInput
	search_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'school-search-name','placeholder': 'Search for a school...'}), label='', max_length=100, min_length=5)

class SchoolSelectForm(forms.Form):
	# Name of the select box. Selection field can be Select, SelectMultiple, CheckboxInput, CheckboxSelectMultiple, or RadioSelect
	school_options = forms.ChoiceField(widget=forms.Select(attrs={'id': 'school-select-name', 'size':'2',}), choices = [], required=False)

class SportSelectForm(forms.Form):
	sport_options = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'id': 'sport-select-name'}), label='', queryset=Sport.objects.all(), required=True)


class BaseballForm(ModelForm):

	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    self.fields['position'].widget.attrs.update({'class': 'Form-Select'})
	    self.fields['year'].widget.attrs.update({'class': 'Form-Select'})
	class Meta:
		model = Baseball
		exclude = ['id', 'user']
class BasketBallForm(ModelForm):

	class Meta:
		model = Basketball
		exclude = ['id', 'user']
class BowlingForm(ModelForm):

	class Meta:
		model = Bowling
		exclude = ['id', 'user']
class CheerleadingForm(ModelForm):
	class Meta:
		model=Cheerleading
		exclude = ['id', 'user']
class Cross_CountryForm(ModelForm):

	class Meta:
		model = Cross_Country
		exclude = ['id', 'user']
class Field_HockeyForm(ModelForm):

	class Meta:
		model = Field_Hockey
		exclude = ['id', 'user']
class FootballForm(ModelForm):

	class Meta:
		model = Football
		exclude = ['id', 'user']
class GolfForm(ModelForm):

	class Meta:
		model = Golf
		exclude = ['id', 'user']
class GymnasticsForm(ModelForm):

	class Meta:
		model = Gymnastics
		exclude = ['id', 'user']
class Ice_HockeyForm(ModelForm):

	class Meta:
		model = Ice_Hockey
		exclude = ['id', 'user']
class SoccerForm(ModelForm):

	class Meta:
		model = Soccer
		exclude = ['id', 'user']
class SoftballForm(ModelForm):

	class Meta:
		model = Soccer
		exclude = ['id', 'user']
class SwimmingForm(ModelForm):

	class Meta:
		model = Swimming
		exclude = ['id', 'user']
class TennisForm(ModelForm):

	class Meta:
		model = Tennis
		exclude = ['id', 'user']
class Track_And_FieldForm(ModelForm):

	class Meta:
		model = Track_And_Field
		exclude = ['id', 'user']
class VolleyballForm(ModelForm):

	class Meta:
		model = Volleyball
		exclude = ['id', 'user']
class WrestlingForm(ModelForm):

	class Meta:
		model = Wrestling
		exclude = ['id', 'user']
