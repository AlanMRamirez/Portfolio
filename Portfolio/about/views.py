from django.shortcuts import render
from django.views.generic import ListView
from .models import InfoAbout

# Create your views here.

class AboutListView(ListView):
    model = InfoAbout
    context_object_name = "info_about"


