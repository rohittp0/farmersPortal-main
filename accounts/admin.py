from django.contrib import admin

from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ["username", "first_name"]
    list_display = ["first_name", 'last_name', 'net_worth' ]
    list_filter = ['is_admin', "is_farmer", "is_employee"]
