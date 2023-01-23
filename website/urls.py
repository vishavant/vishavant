from django.urls import path
from website import views

app_name = "website"

urlpatterns = [
    path('', views.homepage, name='home'),
    path('projects/', views.display_projects, name='projects'),
    path('blogs/', views.display_blogs, name='blogs'),
    path('contact-me/', views.contact_me, name='contact-me'),
]
