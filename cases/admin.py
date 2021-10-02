from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from .models import *


User = get_user_model()


class ClaimAdmin(admin.ModelAdmin):
    list_display = ["claim_type", "case_status", "handler", "opened_date", "closed_date", "opened_by"]
    search_fields = ["claim_type", "case_status", "handler", "opened_by"]


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Claim, ClaimAdmin)