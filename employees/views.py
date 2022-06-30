from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from accounts.models import User
from employees.forms import EmployeesSignUpForm
from employees.models import Hearing

# Create your views here.


def index(request):
    return render(request, 'employees/index.html')


def EmployeesRegisterViews(request):
    form = EmployeesSignUpForm(request.POST or None)
    message = None
    if request.method == 'POST':
        form = EmployeesSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            message = 'user created'
            return redirect('login')
        else:
            message = 'form is not valid'
    else:
        form = EmployeesSignUpForm()
        print("in else")
    connext = {"form": form, "message": message}
    return render(request, "farmers/register.html", connext)


def HiringRequestList(request):
    hiring_request_lists = Hearing.objects.filter(email=request.user.email)
    return render(request, "employees/hiring-request-list.html", {'hiring_request_lists': hiring_request_lists})


def RejectedJob(request, id):
    hearing = Hearing.objects.get(pk=id)
    hearing.jobHearingStatus = "rejected"
    hearing.save()
    user = User.objects.get(pk=request.user.id)
    user.is_available_for_employment = True
    user.save()
    return redirect('employee_hiring_request_list')


def AcceptedJob(request, id):
    hearing = Hearing.objects.get(pk=id)
    hearing.jobHearingStatus = "accepted"
    hearing.save()
    user = User.objects.get(pk=request.user.id)
    user.is_available_for_employment = False
    user.save()
    return redirect('employee_hiring_request_list')
