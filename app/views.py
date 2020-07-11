from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return HttpResponse('Home Page')


def profile(request):
    return HttpResponse('Profile Page')


def chat(request):
    return HttpResponse('Chat Page')
