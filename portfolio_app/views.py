from django.shortcuts import render
from .models import Project, WorkExperience

# Create your views here.
def home(request):
    project = Project.objects.all()
    workexperience = WorkExperience.objects.all()
    return render(request, 'home.html', {'projects':project, 'workexperience': workexperience})