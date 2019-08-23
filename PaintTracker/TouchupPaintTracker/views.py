from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World")

def paint(request):
    return HttpResponse("list Paint Here")
# Create your views here.
