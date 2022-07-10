from django.shortcuts import render

# Create your views here.
from farmers.models import Job


def index(request):
    context = {"jobs": Job.objects.all(),
               "job_count": Job.objects.all().count(),
               "employees": sum([job.hired_list.count() for job in Job.objects.all()])


               }
    return render(request, 'admins/index.html', context=context)
