from django.shortcuts import redirect, render, get_list_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User
from accounts.views import logout
from admins.models import Announcements, Crop, Weather, Homepage
from employees.models import Hearing
from farmers.forms import FarmerDetailsForm, FarmerSignUpForm, HiringEmployeeForm
from farmers.models import FarmerCropDetails, HiringRequest, Job


# Create your views here.


@login_required
def index(request):
    context = {"anns": Announcements.objects.all(), }
    if Homepage.objects.all().exists():
        context["market_rate"] = Homepage.objects.last().market_rate_link
        context["forum"] = Homepage.objects.last().forum_link

    if Weather.objects.all().exists():
        context["weather"] = Weather.objects.all().last()
        print(context)
    return render(request, 'farmers/index.html', context)


@login_required
def create(request):
    context = {"anns": Job.objects.filter(user=request.user), }
    if request.method == "POST":
        j_name = request.POST['jobname']
        j_desc = request.POST['jdesc']
        j_salary = request.POST["salary"]
        j_day = request.POST['day']
        print(j_day, j_desc, j_name, j_salary)
        if j_name and j_desc and j_salary and j_day:
            job = Job.objects.create(user=request.user, name=j_name, salary=j_salary, description=j_desc, day=j_day)
            context["msg"] = "Job created successfully"
        else:
            context['err'] = "please enter all details"

    return render(request, 'farmers/create_job.html', context)


def FarmersRegisterViews(request):
    form = FarmerSignUpForm(request.POST or None)
    crops = Crop.objects.all()
    message = None
    if request.method == 'POST':
        form = FarmerSignUpForm(request.POST)
        if form.is_valid():
            try:
                if form.is_valid():
                    user = form.save()
                    crop = request.POST['cars']
                    user.corps = Crop.objects.get(id=crop)
                    user.save()
                    message = 'user created'
                    return redirect('/')
            except:
                message = "username already exists"

        else:
            message = 'form is not valid'
    else:
        form = FarmerSignUpForm()
        print("in else")
    connext = {"form": form, "message": message, "crops": crops}
    return render(request, "farmers/register.html", connext)


@login_required
def FarmersAnnouncementsPage(request):
    if not request.user.is_farmer:
        logout(request)
        return redirect("login")
    all_announcements = Announcements.objects.all()
    return render(request, "farmers/announcements.html", {'all_announcements': all_announcements})


@login_required
def EmployeeListPage(request):
    if not request.user.is_farmer:
        logout(request)
        return redirect("login")
    employees = User.objects.filter(
        is_employee=True, is_available_for_job=True)
    return render(request, "farmers/employee-list.html", {'employees': employees})


@login_required
def HiringEmployeePage(request, email):
    if not request.user.is_farmer:
        logout(request)
        return redirect("login")
    form = HiringEmployeeForm(request.POST or None, initial={
        'email': email, 'email_hearing_by': request.user.email})
    if request.method == 'POST':
        form = HiringEmployeeForm(request.POST)
        print(request.user.email)
        if form.is_valid():
            email = form.data['email']
            message = form.data['message']
            email_hearing_by = request.user.email
            Hearing.objects.create(
                email=email, message=message, email_hearing_by=email_hearing_by
            )
            return redirect('employee_list')
    return render(request, "farmers/hiring-employee.html", {'form': form})


@login_required
def FarmerCropListPage(request):
    context = {'crops': FarmerCropDetails.objects.filter(
        user=request.user)}
    return render(request, "farmers/crop-list.html", context)


@login_required
def FarmerCropDelete(request, id):
    crop = FarmerCropDetails.objects.get(pk=id)
    crop.delete()
    return redirect('crop_list')


@login_required
def FarmerCropDetailsPage(request, id=0):
    if not request.user.is_farmer:
        logout(request)
        return redirect("login")
    if request.method == "GET":
        if id == 0:
            form = FarmerDetailsForm()
        else:
            farmerCropDetails = FarmerCropDetails.objects.get(pk=id)
            form = FarmerDetailsForm(instance=farmerCropDetails)
        return render(request, "farmers/farmer-add-crop-details.html", {'form': form})
    if request.method == 'POST':
        if id == 0:
            form = FarmerDetailsForm(request.POST)
        else:
            farmerCropDetails = FarmerCropDetails.objects.get(pk=id)
            form = FarmerDetailsForm(request.POST, instance=farmerCropDetails)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('crop_list')


@login_required
def HiringRequestList(request, id):
    if not request.user.is_farmer:
        logout(request)
        return redirect("login")
    hiring_requests = Job.objects.get(id=id).applications.all()

    return render(request, "farmers/hiring-request-list.html", {'hiring_requests': hiring_requests})


@login_required
def DeleteHiredUser(request, id):
    hearing = Hearing.objects.get(pk=id)
    hearing.delete()
    return redirect('farmers_hiring_request_list')


@login_required
def FarmersWeatherReportPage(request):
    if not request.user.is_farmer:
        logout(request)
        return redirect("login")
    all_weather_report = Weather.objects.all()
    return render(request, "farmers/weather-report.html", {'all_weather_report': all_weather_report})


@login_required
def profile(request):
    try:
        corps = FarmerCropDetails.objects.get(user=request.user)
        context = {"corps": corps}
    except Exception as e:
        context = {}
    try:
        print(request.user.corps.crop_name)
        context['net_worth'] = request.user.hector * request.user.corps.yield_per_hector * request.user.corps.crop_price
    except Exception as e:
        print(e)
    context["anns"] = Announcements.objects.all()

    return render(request, "farmers/profile.html", context=context)


@login_required
def employee_hire(request, id):
    job = Job.objects.get(id=id)
    if request.method == "POST":
        eid = request.POST["employee"]
        e_type = request.POST["type"]
        user = User.objects.get(id=eid)
        try:
            if e_type == "hire":
                job.hired_list.add(user)
                job.applications.remove(user)
            else:
                job.hired_list.remove(user)
        except Exception as e:
            pass

    context = {"employees": job.applications.all(), "hired": job.hired_list.all()}
    return render(request, "farmers/hiring-employee.html", context)
