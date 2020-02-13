from django.shortcuts import render, redirect, HttpResponse
from accounts_app.forms import RegistrationForm

def About(request):
	template_name = 'dashboard_app/About.html'
	return render(request, template_name)
def Blog(request):
	template_name = 'dashboard_app/Blog.html'
	return render(request, template_name)
def Home(request):
	form_class = RegistrationForm
	template_name = 'dashboard_app/Home.html'
	return render(request, template_name, {'form': form_class})
def Sports(request):
	pass
def Dashboard(request):
	return render(request, "dashboard_app/Dashboard.html")
