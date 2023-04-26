from django.contrib import admin

# Register your models here.
from .models import Profile , UserNumbers , UserAdress


admin.site.register(Profile)
admin.site.register(UserNumbers)
admin.site.register(UserAdress)