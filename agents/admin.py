from django.contrib import admin

from . import models


class AgentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "agent_type", "main_phone", "email", "status"]
    list_display_links = ["id", "name", "main_phone", "email"]
    search_fields = ["name", "agent_type", "main_phone", "email", "status"]


admin.site.register(models.Agent, AgentAdmin)