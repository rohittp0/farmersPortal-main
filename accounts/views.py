from accounts.forms import LoginForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout as auth_logout, login


# Create your views here.


# @login_required
def index(request):
    return render(request, 'accounts/new_index.html')


@login_required
def app_api_urls(request):
    return render(request, 'accounts/api-urls.html')


def logout(request):
    auth_logout(request)
    return redirect('/')


def get_succes_link(user):
    if user.is_farmer:
        return "/farmers/"
    elif user.is_superuser:
        return "/admin/"
    elif user.is_employee:
        return "/employee/"


def auth_login(request):
    if request.user.is_authenticated:
        return redirect(get_succes_link(request.user))
    form = LoginForm(request.POST or None)
    message = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(get_succes_link(user))
            else:
                message = 'invalid credentials'
        else:
            message = 'error validating form'
    connext = {'form': form, 'message': message}
    return render(request, 'accounts/login.html', connext)
