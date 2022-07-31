from django.shortcuts import render
from django.views.generic import ListView
from .models import Project, ProjectMiniature
# Create your views here.

class ProjectsListView(ListView):
    model = Project
    context_object_name = "projects"

#class ProjectsBestListView(ListView):
#    model = ProjectMiniature
#    context_object_name = "projects_miniature"





