from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models


# Create your views here.

def home(request):
    post = models.Post.objects.all()
    comments = models.Comment.objects.all()
    context = {'posts': post, 'comments': comments}
    return render(request, 'home.html', context=context)


def profile(request):
    return HttpResponse('Profile Page')


def chat(request):
    return HttpResponse('Chat Page')


def add_post(request):
    return render(request, 'add_post.html')


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
            like_obj = models.Like.objects.get(post_id=post_id,username=request.user)
            print('1')
            if not like_obj.liked:
                post_obj.total_likes += 1
                post_obj.save()
                print('2')
            print('3')
            return redirect('home')
        except:
            print('4')
            like = models.Like(
                post_id=post_id,
                username=request.user,
                liked=True
            )
            like.save()
            print('5')
            post_obj.total_likes += 1
            post_obj.save()
            return redirect('home')

    return redirect('home')
