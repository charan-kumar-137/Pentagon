from django.http import HttpResponse
from django.shortcuts import render
from . import models


# Create your views here.

def home(request):
    post = models.Post.objects.all()
    comments = models.Comment.objects.all()
    context = {'posts': post,'comments':comments}
    return render(request, 'home.html', context=context)


def profile(request):
    return HttpResponse('Profile Page')


def chat(request):
    return HttpResponse('Chat Page')


def add_post(request):
    return render(request,'add_post.html')


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
