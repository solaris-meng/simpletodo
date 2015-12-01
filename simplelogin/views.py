from django.shortcuts import render

from django.template import RequestContext, loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
import traceback

# Create your views here.
def login_login_view(request):
    ctx = {}
    ctx['name'] = 'Meng'
    context = RequestContext(request, ctx)
    template = loader.get_template('login/login.html')
    return HttpResponse(template.render(context))

def login_logout_view(request):
    logout(request)
    return redirect('/')

def login_login_handler(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return redirect('/')
            else:
                # Return a 'disabled account' error message ...
                return HttpResponse('Error, disable account')
        else:
            # Return an 'invalid login' error message. ...
            return HttpResponse('Error, invalid login')
    return HttpResponse('Error')

def login_register_view(request):
    ctx = {}
    ctx['name'] = 'Meng'
    context = RequestContext(request, ctx)
    template = loader.get_template('login/register.html')
    return HttpResponse(template.render(context))

def login_register_handler(request):
    print request.POST
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            user_check = User.objects.filter(username=username)
            if user_check:
                return HttpResponse('Sorry, the user name already registered.')

            user = User.objects.create_user(username, email, password)
            if user is not None:
                # Redirect to a success page.
                return HttpResponse('success')
            else:
                # Return an 'invalid login' error message. ...
                return HttpResponse('Error, invalid register')
        except Exception, e:
            err = traceback.format_exc()
            print err
            return HttpResponse('Error, %s' % err)
    return HttpResponse('invalid')
