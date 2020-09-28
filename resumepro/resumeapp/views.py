from django.shortcuts import render
from .models import EnquaryData
from .forms import EnquryForm
from django.http.response import HttpResponse
def EnquryView(request):
    if request.method=="POST":
        eform=EnquryForm(request.POST)
        if eform.is_valid():
            firstname=request.POST.get('firstname')
            middlename=request.POST.get('middlename')
            lastname = request.POST.get('lastname')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            location=request.POST.get('location')
            gender=eform.cleaned_data.get('gender')


            data=EnquaryData(
                firstname=firstname,
                middlename=middlename,
                lastname=lastname,
                email=email,
                mobile=mobile,
                location=location,
                gender=gender,

            )
            data.save()
            eform=EnquryForm()
            return render(request,'enqury.html',{'eform':eform})
        else:
            return HttpResponse("user Invaild Data")
    else:
        eform=EnquryForm()
        return render(request,'enqury.html',{'eform':eform})