from django.contrib import admin

from .models import *


class VehicleAdmin(admin.ModelAdmin):
    list_display = ["make", "model", "vehicle_status", "currently_reserved", "last_recorded_mileage", "category", "depot", "color", "cc", "fuel_type", "insurance_group"]


admin.site.register(Vehicle, VehicleAdmin)