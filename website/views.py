from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, "website/homepage.html")


def display_projects(request):
    return render(request, "website/display_projects.html")


def display_blogs(request):
    return render(request, "website/display_blogs.html")


def contact_me(request):
    return render(request, "website/contact_me.html")