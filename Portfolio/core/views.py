from django.shortcuts import render, HttpResponse

# Create your views here.

def Home(request):
    return render(request, 'core/index.html')


def About(request):
    return render(request, 'core/about.html')

