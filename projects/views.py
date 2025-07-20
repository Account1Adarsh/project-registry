# projects/views.py

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Project

from django.db.models import Q
from django.views.generic import ListView
from .models import Project

class ProjectListView(ListView):
    model               = Project
    template_name       = 'projects/project_list.html'
    context_object_name = 'projects'
    paginate_by         = 20

    def get_queryset(self):
        qs = Project.objects.all().order_by('-created_at')

        # -- Optional free‐text search (title OR link) --
        q = self.request.GET.get('q','').strip()
        if q:
            qs = qs.filter(
                Q(title__icontains=q) |
                Q(link__icontains=q)
            )

        # -- Optional filters --
        year   = self.request.GET.get('year')
        branch = self.request.GET.get('branch')
        ptype  = self.request.GET.get('type')

        if year:
            qs = qs.filter(year=year)
        if branch:
            qs = qs.filter(branch=branch)
        if ptype in dict(Project._meta.get_field('project_type').choices):
            qs = qs.filter(project_type=ptype)

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Echo back form values
        ctx.update({
            'filter_q':      self.request.GET.get('q',''),
            'filter_year':   self.request.GET.get('year',''),
            'filter_branch': self.request.GET.get('branch',''),
            'filter_type':   self.request.GET.get('type',''),
            # Dropdown options
            'all_years':     Project.objects.order_by('year').values_list('year', flat=True).distinct(),
            'all_branches':  Project.objects.order_by('branch').values_list('branch', flat=True).distinct(),
            'all_types':     Project._meta.get_field('project_type').choices,
        })
        return ctx

class ProjectCreateView(CreateView):
    model         = Project
    fields        = ['title', 'link', 'year', 'batch', 'branch', 'project_type']
    success_url   = reverse_lazy('project_list')
