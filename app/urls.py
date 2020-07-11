from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('chat', views.chat, name='chat'),
]
