from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from accounts.models import User
from admins.models import Announcements
from employees.forms import EmployeesSignUpForm
from employees.models import Hearing

# Create your views here.
from farmers.models import HiringRequest


def index(request):
    anns = Announcements.objects.all()
    # print(anns)
    reqs = HiringRequest.objects.filter(to_user=request.user).exclude(accepted=True)
    return render(request, 'employees/index.html', {"anns": anns, "reqs": reqs})


def EmployeesRegisterViews(request):
    form = EmployeesSignUpForm(request.POST or None)
    message = None
    if request.method == 'POST':
        form = EmployeesSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            message = 'user created'
            return redirect('/')
        else:
            message = 'form is not valid'
    else:
        form = EmployeesSignUpForm()
        print("in else")
    connext = {"form": form, "message": message}
    return render(request, "employees/register.html", connext)


def HiringRequestList(request):
    hiring_request_lists = Hearing.objects.filter(email=request.user.email)
    return render(request, "employees/hiring-request-list.html", {'hiring_request_lists': hiring_request_lists})


def rejected_job(request):
    print(request)
    if request.method == "POST":
        try:
            hearing = HiringRequest.objects.get(pk=request.POST["id"])
            hearing.rejected = True
            print(hearing)
            hearing.save()
        except Exception as e:
            print(e)
    return redirect('/employee/')


def accepted_job(request):
    print(request)
    if request.method == "POST":
        try:
            hearing = HiringRequest.objects.get(pk=request.POST["id"])
            print(hearing)
            hearing.accepted = True
            hearing.save()
            request.user.is_available_for_job = False
            request.user.save()
        except Exception as e:
            print(e)
    return redirect('/employee/')


@login_required()
def profile(request):
    anns = Announcements.objects.all()
    # print(anns)
    return render(request, "employees/profile.html", {"anns": anns})
