from django.contrib import admin

from admins.models import Announcements, Crop, Weather, Homepage

admin.site.register(Announcements)
admin.site.register(Weather)
admin.site.register(Crop)
admin.site.register(Homepage)
