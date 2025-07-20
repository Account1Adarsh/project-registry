from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "branch", "project_type")
    list_filter = ("year", "branch", "project_type")
    search_fields = ("title", "link")
