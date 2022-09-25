from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse

# Create your views here.

def first(request):
    return HttpResponse("hello brainworks")

def second(request):
    return HttpResponse("we are learning python")