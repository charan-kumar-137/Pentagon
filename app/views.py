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

        return HttpResponse('success post added')

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
