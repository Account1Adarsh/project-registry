from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "link", "year", "level", "branch", "project_type", "enrollment_number"]
