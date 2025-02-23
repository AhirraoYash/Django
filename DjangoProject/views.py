from django.http import HttpResponse
from django.shortcuts import render #reader html page

def home(request):
    # return HttpResponse("hello, world this is home")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("hello, world this is about")


def contact(request):
    return HttpResponse("hello, world this is contact")