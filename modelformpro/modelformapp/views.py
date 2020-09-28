from django.shortcuts import render
from django.http.response import HttpResponse
from .models import EmpData
from.forms import EmpForm

def empview(request):
    if request.method=="POST":
        eform=EmpForm(request.POST)
        if eform.is_valid():
            eform.save()
            eform=EmpForm()
            return render(request,'empdata.html',{'eform':eform})
        else:
            return HttpResponse("Invalid Data")
    else:
      eform=EmpForm()
      return render(request,'empdata.html',{'eform':eform})
