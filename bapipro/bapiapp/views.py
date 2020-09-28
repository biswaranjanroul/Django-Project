from django.shortcuts import render
from .models import Emp
from .form import EmpForm
from django.http.response import HttpResponse

def empview(request):
    if request.method=='POST':
        eform=EmpForm(request.POST)
        if eform.is_valid():
            name1=request.POST.get('name')
            location1=request.POST.get('location')
            salary1=request.POST.get('salary')
            email1=request.POST.get('email')
            data=Emp(
                name=name1,
                location=location1,
                salary=salary1,
                email=email1
            )
            data.save()
            eform=EmpForm()
            return render(request,'empform.html',{'eform':eform})
        else:
            return HttpResponse('User Invalid Data')
    else:
        eform = EmpForm()
        return render(request, 'empform.html', {'eform': eform})