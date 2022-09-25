from django.shortcuts import render,HttpResponse

# Create your views here.

def first(request):
    return HttpResponse("hello world")

def second(request):
    return HttpResponse("hello team")

