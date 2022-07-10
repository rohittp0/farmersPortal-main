from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from accounts.models import User
from admins.models import Announcements
from employees.forms import EmployeesSignUpForm
from employees.models import Hearing

# Create your views here.
from farmers.models import HiringRequest, Job


@login_required
def index(request):
    anns = Announcements.objects.all()
    # print(anns)
    reqs = Job.objects.all().exclude(applications__in=[request.user]).exclude(hired_list__in=[request.user]) \
        .exclude(declined__in=[request.user])
    return render(request, 'employees/index.html', {"anns": anns, "reqs": reqs})


def EmployeesRegisterViews(request):
    form = EmployeesSignUpForm(request.POST or None)
    message = None
    if request.method == 'POST':
        form = EmployeesSignUpForm(request.POST)
        if form.is_valid():
            if not User.objects.filter(username=form.username).exists():
                user = form.save()
                message = 'user created'
                return redirect('/')
            message = "username already exists"
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

            job = Job.objects.get(pk=request.POST["id"])
            job.applications.remove(request.user)
            job.declined.add(request.user)
        except Exception as e:
            print(e)
    return redirect('/employee/')


def accepted_job(request):
    print(request)
    if request.method == "POST":
        try:
            job = Job.objects.get(pk=request.POST["id"])
            job.applications.add(request.user)
        except Exception as e:
            print(e)
    return redirect('/employee/')


@login_required()
def profile(request):
    anns = Job.objects.filter(hired_list__in=[request.user])
    # print(anns)
    return render(request, "employees/profile.html", {"anns": anns})
