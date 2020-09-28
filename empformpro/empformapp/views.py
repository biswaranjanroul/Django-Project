from django.shortcuts import render
from .models import Emp
from .forms import Empform
from django.http.response import HttpResponse
def empview(request):
    if request.method=='POST':
        pass
    else:
       eform=Empform()
    return render(request, 'empform.html', {'eform': eform})

