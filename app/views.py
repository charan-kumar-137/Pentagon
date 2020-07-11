from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,'home.html')


def profile(request):
    return HttpResponse('Profile Page')


def chat(request):
    return HttpResponse('Chat Page')
