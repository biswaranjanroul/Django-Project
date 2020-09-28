from django.shortcuts import render
from django.http.response import HttpResponse
from .models import RegistrationData
from .forms import RegistrationForm,LoginForm
def reg_view(request):
    if request.method == "POST":
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')

            data = RegistrationData(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                email=email,
                mobile=mobile
            )
            data.save()
            rform = RegistrationForm()
            return render(request,'reg.html',{'rform':rform})
        else:
            return HttpResponse('User Invalid Data')
    else:
        rform = RegistrationForm()
        return render(request,'reg.html',{'rform':rform})
def login_view(request):
    if request.method == "POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = RegistrationData.objects.filter(username=username)
            pwd = RegistrationData.objects.filter(password=password)
            if user and pwd:
                return HttpResponse("Login Success")
            else:
                return HttpResponse("Login Failed")
        else:
            return HttpResponse("User Invalid Data")
    else:
        lform = LoginForm()
        return render(request,'login.html',{'lform':lform})

