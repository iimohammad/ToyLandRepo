from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone_number', 'is_staff')
    search_fields = ('username', 'email', 'phone_number')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



