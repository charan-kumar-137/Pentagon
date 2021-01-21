from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
import django.contrib.auth as djauth

from . import models


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        post = models.Post.objects.all()
        comments = models.PostComment.objects.all()
        nav = [
            ['/', 'Pentagon'],
            ['profile', 'Profile'],
            ['add_post', 'Post'],
            ['chat', 'Chat'],
            ['logout', 'Logout'],
        ]
        context = {'posts': post, 'comments': comments, 'navs': nav, 'user': request.user}
        return render(request, 'home.html', context=context)

    return redirect('login')


def profile(request):
    if request.user.is_authenticated:
        nav = [
            ['/', 'Pentagon'],
            ['profile', 'Profile'],
            ['add_post', 'Post'],
            ['chat', 'Chat'],
            ['logout', 'Logout'],
        ]
        user = models.User.objects.get(username=request.user)
        context = {'navs': nav, 'user': user}
        return render(request, 'profile.html', context=context)

    return redirect('login')


def chat(request):
    if request.user.is_authenticated:
        nav = [
            ['/', 'Pentagon'],
            ['profile', 'Profile'],
            ['add_post', 'Post'],
            ['chat', 'Chat'],
            ['logout', 'Logout'],
        ]
        context = {'navs': nav, 'user': request.user}
        return render(request, 'chat.html', context=context)

    return redirect('login')


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
            ['chat', 'Chat'],
            ['add_post', 'Post'],
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

        user = models.User.objects.get(username=request.user)
        user.total_posts += 1
        user.save()

        return redirect('/')

    return HttpResponse('Post add fail')


def handle_added_comment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment', '')
        post_id = request.POST.get('post_id', '')

        comment_obj = models.PostComment(
            username=request.user,
            post_id=post_id,
            description=comment
        )
        comment_obj.save()

        post = models.Post.objects.get(post_id=post_id)
        post.total_comments += 1
        post.save()

        user = models.User.objects.get(username=request.user)
        user.total_comments += 1
        user.save()

        return redirect('home')

    return redirect('home')


def handle_added_like(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = models.Post.objects.get(post_id=post_id)

        try:
            like_obj = models.PostLike.objects.get(post_id=post_id, username=request.user)
            if not like_obj.liked:
                post_obj.total_likes += 1
                post_obj.save()

                user = models.User.objects.get(username=request.user)
                user.total_likes += 1
                user.save()

            return redirect('home')
        except:
            like = models.PostLike(
                post_id=post_id,
                username=request.user,
                liked=True
            )
            like.save()

            post_obj.total_likes += 1
            post_obj.save()

            user = models.User.objects.get(username=request.user)
            user.total_likes += 1
            user.save()

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

            user_info = models.User(
                username=username,
                name=name,
                email=email
            )
            user_info.save()

            user = djauth.authenticate(request, username=username, password=password)
            djauth.login(request, user=user)
            return redirect('/')
        except:
            return redirect('signup')

    return redirect('signup')


def handle_chat_search(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            receiver = request.POST.get('username', ' ')
            try:
                user_obj = User.objects.get(username=receiver)
                user_obj.save()
            except:

                return redirect('chat')

            sender = request.user
            if receiver == sender.username:
                return redirect('chat')

            try:
                chat = models.Chat.objects.get(sender=sender.username, receiver=receiver)
            except:
                try:
                    chat = models.Chat.objects.get(sender=receiver, receiver=sender.username)
                except:
                    chat = models.Chat(
                        sender=sender.username,
                        receiver=receiver
                    )
                    chat.save()

            messages = models.ChatMessage.objects.filter(cid=chat.cid)
            nav = [
                ['/', 'Pentagon'],
                ['profile', 'Profile'],
                ['add_post', 'Post'],
                ['chat', 'Chat'],
                ['logout', 'Logout']
            ]
            context = {
                'navs': nav,
                'user': request.user,
                'messages': messages,
                'receiver': receiver,
                'isreceiver': True
            }

            return render(request, 'chat.html', context=context)

    return redirect('home')


def handle_chat_message(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            sender = request.POST.get('sender', '')
            receiver = request.POST.get('receiver', '')
            message = request.POST.get('message', '')
            try:
                chat = models.Chat.objects.get(sender=sender, receiver=receiver)
            except:
                chat = models.Chat.objects.get(sender=receiver, receiver=sender)
            chat_message = models.ChatMessage(
                user=sender,
                cid=chat.cid,
                message=message
            )
            chat_message.save()
            messages = models.ChatMessage.objects.filter(cid=chat.cid)
            nav = [
                ['/', 'Pentagon'],
                ['profile', 'Profile'],
                ['add_post', 'Post'],
                ['chat', 'Chat'],
                ['logout', 'Logout'],
            ]
            context = {
                'navs': nav,
                'user': request.user,
                'messages': messages,
                'receiver': receiver,
                'isreceiver': True
            }

            return render(request, 'chat.html', context=context)

    return redirect('home')
