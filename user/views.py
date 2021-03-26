from django.shortcuts import render
from views import Project, JobHistory
# Create your views here.


class Sample(request):
    project = Project.objects.all()
    print(project)