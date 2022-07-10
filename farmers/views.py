from django.shortcuts import redirect, render, get_list_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User
from admins.models import Announcements, Crop, Weather, Homepage
from farmers.forms import FarmerSignUpForm
from farmers.models import Job, FarmerCropDetails


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
        start_date = request.POST['start_date']
        end_date = request.POST["end_date"]
        print(j_day, j_desc, j_name, j_salary)
        if j_name and j_desc and j_salary and j_day:
            job = Job.objects.create(user=request.user, name=j_name, salary=j_salary, description=j_desc, day=j_day,
                                     start_date=start_date, end_date=end_date)
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
