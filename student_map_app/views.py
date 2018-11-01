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
        if form.is_valid():
            if request.user.is_authenticated:
                User_School.objects.create(student_id=request.user, school_id=School.objects.get(school_name=form.cleaned_data['school_options']))
                #myUser = User_School.objects.get(student_id=request.user)

                #myUser.
                return HttpResponseRedirect("https://worldstarhiphop.com")
    else:
        form = SchoolSelectForm(request.GET)
        # Form.fields['school_options'] takes a list OR a tuple,
        # this filter returns a list itself. I need to return the results of this filter as a tuple and pass it to the field
        # "choice" alone returns the school id and the school name. The choice.school_name essentially does nothing in this case
        form.fields['school_options'].choices = [(choice.school_name, choice) for choice in School.objects.filter(school_name__icontains=search_data)]

    return render(request, 'student_map_app/School_Select.html', {'form': form })

def SportSelect(request):
    pass
    # Would like a multiplechoice field Here
    # Make a multiple chocie field Access the User_School.school_id.ss_sports_id
