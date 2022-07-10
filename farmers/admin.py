from django.contrib import admin

from farmers.models import FarmerCropDetails, HiringRequest, Job

admin.site.register(HiringRequest)
admin.site.register(Job)
