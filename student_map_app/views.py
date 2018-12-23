from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .forms import SchoolSearchForm, SchoolSelectForm
from scholarship_map.models import User_School, School

def SchoolLanding(request):
    template = 'student_map_app/School_Landing.html'
    return render(request, template)

def SchoolSearch(request):
    if request.method == 'POST':
        form = SchoolSearchForm(request.POST)
        if form.is_valid(): # We only have the school_search field, so how does this form fail validation?
            request.session['school_search'] = request.POST['school_search'] # Storing the user's string in the session to be accessed between pages
            return HttpResponseRedirect('../select/') # Take user to the select form
        else:
            print(form.errors)
    else:
        form = SchoolSearchForm()

    return render(request, 'student_map_app/School_Search.html', {'form': form})

def SchoolSelect(request):
    search_data = request.session['school_search']
    if request.method == 'POST':
        form = SchoolSelectForm(request.POST)
        selectedChoice = request.POST.get('school_options') # Get the value of what was sent
        form.fields['school_options'].choices = [(selectedChoice, selectedChoice)] # This is (Jamestown, Jamestown). Choices are evaluated through tuples
        if form.is_valid():
            if request.user.is_authenticated:
                User_School.objects.create(student_id=request.user, school_id=School.objects.get(school_name=form.cleaned_data['school_options']))
    else:
        form = SchoolSelectForm()
        # Form.fields['school_opt
        form.fields['school_options'].choices = [(choice.school_name, choice) for choice in School.objects.filter(school_name__icontains=search_data)]
        # form.fields['school_options'].choices = [(choice.school_name, choice) for choice in School.objects.filter(school_name__icontains=search_data)]
    return render(request, 'student_map_app/School_Select.html', {'form': form })

def SportSelect(request):
    pass
    # Would like a multiplechoice field Here
    # Make a multiple chocie field Access the User_School.school_id.ss_sports_id
