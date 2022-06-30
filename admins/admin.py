from django.contrib import admin

from admins.models import Announcements, Crop, Weather

admin.site.register(Announcements)
admin.site.register(Weather)
admin.site.register(Crop)
