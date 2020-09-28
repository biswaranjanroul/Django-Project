from django.shortcuts import render
from django.http.response import HttpResponse
def hyd(request):
    x="Hyd provides all course for less fee"
    return HttpResponse(x)
def bang(request):
    y="Bang provides jobs for all students"
    return HttpResponse(y)
def chennai(request):
    x="Chennai gives for local people"
    return HttpResponse(x)