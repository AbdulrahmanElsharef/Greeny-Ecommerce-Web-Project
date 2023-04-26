from django.contrib import admin

# Register your models here.

from .models import DeliveryFee , Company



admin.site.register(DeliveryFee)
admin.site.register(Company)