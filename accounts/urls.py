from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path('login', views.user_login, name="login"),
    path('signup', views.user_signup, name="signup"),
    path('profile', views.user_profile, name="profile"),  
]
