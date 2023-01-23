from django.shortcuts import render

# Create your views here.

def user_login(request):
    return render(request, "accounts/user_login.html")


def user_signup(request):
    return render(request, "user_registration.html")


def user_logout(request):
    pass

def user_profile(request):
    return render(request, "accounts/user_profile.html")

