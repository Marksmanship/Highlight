from django import forms

class SchoolSearchForm(forms.Form):
	school_search = forms.CharField(max_length=100, min_length=5)

	def __init__(self, *args, **kwargs):
		super(SchoolSearchForm, self).__init__(*args, **kwargs)
		self.fields['school_search'].widget.attrs={'id': 'school-search-box',} # Name of search box not form
class SchoolSelectForm(forms.Form):
		school_options = forms.ChoiceField(choices = [], required=False)
