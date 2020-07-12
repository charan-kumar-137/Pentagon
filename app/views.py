from django.http import HttpResponse
from django.shortcuts import render
from . import models


# Create your views here.

def home(request):
    post = models.Post.objects.all()
    context = {'posts': post}
    return render(request, 'home.html', context=context)


def profile(request):
    return HttpResponse('Profile Page')


def chat(request):
    return HttpResponse('Chat Page')
