from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from . import models


User = get_user_model()

class AgentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "agent_type", "main_phone", "email", "status"]


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(models.Agent, AgentAdmin)