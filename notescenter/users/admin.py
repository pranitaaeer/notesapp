from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomeUser
# Register your models here.
admin.site.register(CustomeUser,UserAdmin)
