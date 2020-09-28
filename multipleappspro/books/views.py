from django.shortcuts import render
from django.http.response import HttpResponse
def python(request):
    x="python is simple and easy Language"
    return HttpResponse(x)
def django(request):
    y="Django is also very very simple framework of python language"
    return HttpResponse(y)
def ui(request):
    x="UI is most impornat for webdevelopement"
    return HttpResponse(x)
