from django.contrib import admin

from accounts.models import User

admin.site.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = [""]