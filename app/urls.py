from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('chat', views.chat, name='chat'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('add_post', views.add_post, name='add_post'),
    path('handle_added_post', views.handle_added_post, name='handle_added_post'),
    path('handle_added_comment', views.handle_added_comment, name='handle_added_comment'),
    path('handle_added_like', views.handle_added_like, name='handle_added_like'),
    path('handle_user_login', views.handle_user_login, name='handle_user_login'),
    path('handle_user_signup', views.handle_user_signup, name='handle_user_signup'),
]
