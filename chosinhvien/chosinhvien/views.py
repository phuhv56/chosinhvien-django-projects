#__author__ = 'Der Kaiser'
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from chosinhvien.forms import UserCreationForm
from mysite.models import Product


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    context = {'full_name': request.user.username}

    respone = render_to_response('loggedin.html', context)
    respone.set_cookie('user', request.user.username)

    return respone

def invalid(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    products = Product.objects.all().order_by('-time_post')
    context = {'products': products}

    respone = render_to_response('logout.html', context)
    respone.set_cookie('user', '')
    return respone

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/accounts/register_success/")
    else:
        form = UserCreationForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response(
        'register.html', args
    )

def register_success(request):
    return render_to_response('register_success.html')