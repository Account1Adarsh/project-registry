# projects/views.py

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Project

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    ordering = ['-created_at']
    paginate_by = 20

class ProjectCreateView(CreateView):
    model = Project
    fields = ['title', 'link', 'year', 'batch', 'branch', 'project_type']
    success_url = reverse_lazy('project_list')
