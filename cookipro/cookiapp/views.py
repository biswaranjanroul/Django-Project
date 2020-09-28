from django.shortcuts import render
from django.http import HttpResponse
def create_Cookie(request):
    if not request.COOKIES.get('color'):
        response=HttpResponse("cook is created")
        response.set_cookie('color','blue')
        return response
    else:
       return HttpResponse("your favorite""color is {0}".format(request.COOKIES['color']))
def count_Cookie(request, visits=None):
    if not request.COOKIES.get('visits'):
     response=HttpResponse("This is your first vist to the site""from now on I will track""your visits to this site")
     response.set_cookie('visits','1')
    else:
       visits=int(request.COOKIES.get('visits'))+1
       response=HttpResponse("This is your{0} visit".format(visits))
       response.set_cookie('visits',str(visits))
    return response
def delete_Cookie(request):
    if request.COOKIES.get('visits'):
        response=HttpResponse("Cookies cleared")
        response.delete_cookie("visits")
    else:
      response = HttpResponse("we are not tracking you")
    return response





