from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('chat', views.chat, name='chat'),
    path('add_post',views.add_post,name='add_post'),
    path('handle_added_post',views.handle_added_post,name='handle_added_post'),
]
