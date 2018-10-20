from django.shortcuts import redirect
from .forms import SchoolSearchForm, SchoolSelectForm


def SchoolSearch(request):
	if request.method == 'POST':
		form = SchoolSearchForm(request.POST)
        if form.is_valid():
			request.session['school_search'] = request.POST['school_search']
			return redirect('select/')
		else:
			form = SchoolSearchForm()
def SchoolSelect(request):
	if request.method == 'GET':
		search_data = request.session.get('school_search')
		form = SchoolSelectForm()
        if request.user.is_authenticated:
            form.school_options.choices = [(school.school_name) for school in School.objects.filter(school_name__icontains=self.cleaned_data['search_data'])]
		else:
			# User has selected a schoool from the dropdown box
			# We must now match their selected school name to the id
			form=SchoolSelectForm(request.POST) # User's selection is now visible
			if form.is_valid():
				form.save(commit=False)
            	form.student_id = request.user.id
				form.school_id = School.objects.get(id=request.POST['school_options']) #School's id matches User_School's school_id
				form.save()
