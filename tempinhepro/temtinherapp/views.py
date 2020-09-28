from django.shortcuts import render
def home(request):
    return render(request,'myhome.html')
def contact(request):
    return render(request,'mycontacts.html')
def feedback(request):
    return render(request,'myfeedbacks.html')
def gallery(request):
    return render(request,'mygallery.html')
