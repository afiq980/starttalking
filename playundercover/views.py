from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login
from django.template.context_processors import csrf

def home(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'login.html', {})


def authentication(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=email, password=password)

    def error_handle(error):
        c = {}
        c.update(csrf(request))
        return render(request, 'login.html', {'error_message': error})

    if user is not None:

        if user.is_active:
            auth_login(request, user)
            c = {}
            c.update(csrf(request))
            return redirect('home')
        else:
            c = {}
            c.update(csrf(request))
            error = 'Invalid username/password'
            return error_handle(error)
    elif user is None:
        c = {}
        c.update(csrf(request))
        error = 'Invalid username/password'
        return error_handle(error)