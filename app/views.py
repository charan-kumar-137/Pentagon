from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
import django.contrib.auth as djauth

from . import models


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        post = models.Post.objects.all()
        comments = models.Comment.objects.all()
        nav = [
            ['/', 'Pentagon'],
            ['profile', 'Profile'],
            ['chat', 'Chat'],
            ['logout', 'Logout']
        ]
        context = {'posts': post, 'comments': comments, 'navs': nav, 'user': request.user}
        return render(request, 'home.html', context=context)

    return redirect('login')


def profile(request):
    return HttpResponse('Profile Page')


def chat(request):
    return HttpResponse('Chat Page')


def login(request):
    if not request.user.is_authenticated:
        nav = [
            ['/', 'Pentagon']
        ]
        return render(request, 'login.html', context={'navs': nav})

    return redirect('/')


def signup(request):
    if not request.user.is_authenticated:
        nav = [
            ['/', 'Pentagon']
        ]
        return render(request, 'signup.html', context={'navs': nav})

    return redirect('/')


def logout(request):
    if request.user.is_authenticated:
        djauth.logout(request)
        return redirect('/')

    return redirect('/')


def add_post(request):
    if request.user.is_authenticated:
        nav = [
            ['/', 'Pentagon'],
            ['profile', 'Profile'],
            ['chat', 'Chat']
        ]
        return render(request, 'add_post.html', context={'navs': nav})

    return redirect('/')


def handle_added_post(request):
    if request.method == 'POST':
        image = request.FILES.get('image', '')
        description = request.POST.get('description', '')

        post = models.Post(
            image=image,
            username=request.user,
            description=description
        )
        post.save()

        return redirect('/')

    return HttpResponse('Post add fail')


def handle_added_comment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment', '')
        post_id = request.POST.get('post_id', '')

        comment_obj = models.Comment(
            username=request.user,
            post_id=post_id,
            description=comment
        )
        comment_obj.save()

        post = models.Post.objects.get(post_id=post_id)
        post.total_comments += 1
        post.save()

        return redirect('home')

    return redirect('home')


def handle_added_like(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = models.Post.objects.get(post_id=post_id)

        try:
            like_obj = models.Like.objects.get(post_id=post_id, username=request.user)
            if not like_obj.liked:
                post_obj.total_likes += 1
                post_obj.save()

            return redirect('home')
        except:
            like = models.Like(
                post_id=post_id,
                username=request.user,
                liked=True
            )
            like.save()

            post_obj.total_likes += 1
            post_obj.save()
            return redirect('home')

    return redirect('home')


def handle_user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = djauth.authenticate(request, username=username, password=password)
        if user:
            djauth.login(request, user)

            return redirect('/')

    return redirect('login')


def handle_user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.first_name = name
            user.save()

            user = djauth.authenticate(request, username=username, password=password)
            djauth.login(request, user=user)
            return redirect('/')
        except:
            return redirect('signup')

    return redirect('signup')
