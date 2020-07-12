from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('chat', views.chat, name='chat'),
    path('add_post', views.add_post, name='add_post'),
    path('handle_added_post', views.handle_added_post, name='handle_added_post'),
    path('handle_added_comment', views.handle_added_comment, name='handle_added_comment'),
    path('handle_added_like', views.handle_added_like, name='handle_added_like'),
]
