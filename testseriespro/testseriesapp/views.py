from django.shortcuts import render
from django.http.response import HttpResponse
from .models import SignupData
from .forms import SignupForm,loginForm
def signup_view(request):
    if request.method == "POST":
        sform = SignupForm(request.POST)
        if sform.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            password = request.POST.get('password')
            username = request.POST.get('username')

            data = SignupData(
                first_name=first_name,
                last_name=last_name,
                password=password,
                username=username,
               )
            data.save()
            sform = SignupForm()
            return render(request,'signup.html',{'sform':sform})
        else:
            return HttpResponse('User Invalid Data')
    else:
        sform = SignupForm()
        return render(request,'signup.html',{'sform':sform})

def login_view(request):
    if request.method == "POST":
        lform = loginForm(request.POST)
        if lform.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = SignupData.objects.filter(username=username)
            pwd = SignupData.objects.filter(password=password)
            if user and pwd:
                return render(request,'testserieshome.html',{'lform':lform})
            else:
                return HttpResponse("Sign In Failed")
        else:
            return HttpResponse("User Invalid Data")
    else:
        lform = loginForm()
        return render(request,'login.html',{'lform':lform})

def logout_view(request):
    return render(request, 'logout.html')
def test_home(request):
    return render(request, 'testserieshome.html')
def test_home2(request):
    return render(request, 'testserieshome2.html')
def test_home3(request):
    return render(request, 'testserieshome3.html')


def test_desc(request):
    return render(request, 'testdecs.html')








