from django.contrib import admin
from django.templatetags.static import static

from .models import *


class CustomChangeTemplate(admin.ModelAdmin):
    change_form_template = "change_form.html"

    def get_model_perms(self, request):
        return {}
    
    def has_delete_permission(request, obj=None, *args, **kwargs):
        return False

    class Media:
        css = {
            "all": (static("admin/css/mine.css"),)
        }

        js = (
            """https://code.jquery.com/jquery-3.6.0.min.js""",
            static("admin/js/service.js")
        )


class VehicleAdmin(admin.ModelAdmin):
    list_display = ["vrm", "make", "model", "vehicle_status", "currently_reserved", "category", "inner_sub_category", "depot", "cc", "fuel_type", "insurance_cover"]
    exclude = ["hire_details", "service_details", "supplier_details", "finance_details","sale_details"]
    search_fields = ["vehicle_dvla_number", "make", "model", "vehicle_status", "currently_reserved"]

    def vrm(self, obj):
        return obj.vehicle_dvla_number
    vrm.short_description = "VRM"

    class Media:
        js = (
            static("admin/js/dvla.js"),
            """https://code.jquery.com/jquery-3.6.0.min.js"""
        )
        css = {
            "all": (static("admin/css/mine.css"),)
        }

    change_form_template = "change_form.html"


admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Hire,CustomChangeTemplate)
admin.site.register(Service, CustomChangeTemplate)
admin.site.register(Finance, CustomChangeTemplate)
admin.site.register(Sale, CustomChangeTemplate)
admin.site.register(Supplier, CustomChangeTemplate)
admin.site.register(LicensingAuthority, CustomChangeTemplate)