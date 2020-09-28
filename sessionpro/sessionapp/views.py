from django.shortcuts import render
from django.http import HttpResponse
def test_session(request):
    request.session.set_test_cookie()
    return HttpResponse("Session is created in the server")
def test_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response=HttpResponse("session deleted")
    else:
        response=HttpResponse("Session is not available")
    return response
def save_session_data(request):
    request.session['Eno']=1001
    request.session['Ename']='Bapi'
    request.session['Language']='python'
    request.session['Framework']='Django'
    return HttpResponse("Session Data saved")
def access_session_data(request):
    response=" "
    if request.session.get('Eno'):
        response +="Eno :{0} <br>".format(request.session.get('Eno'))
    if request.session.get('Ename'):
        response +="Ename :{0} <br>".format(request.session.get('Ename'))
    if request.session.get('Language'):
        response += " Language:{0} <br>".format(request.session.get('Language'))
    if request.session.get('Framework'):
        response += " Framework:{0} <br>".format(request.session.get('Framework'))
    if not response:
        return HttpResponse("NO session data")
    else:
        return HttpResponse(response)
def delete_session_data(request):
    try:
        del request.session['Eno']
        del request.session['Ename']
        del request.session['Language']
        del request.session['Framework']
    except KeyError:
         pass
    return HttpResponse("Session Data cleared")