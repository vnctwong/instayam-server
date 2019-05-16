from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'is_private')


# Register your models here.
admin.site.register(User, UserAdmin)
