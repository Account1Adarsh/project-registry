from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Project
from .forms import ProjectForm

class AdminRequiredMixin(UserPassesTestMixin):
    """
    Only allow access if the user is staff (is_staff=True).
    """
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        # you could redirect to login or raise 403
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied




class ProjectListView(ListView):
    model = Project
    paginate_by = 10
    template_name = "projects/project_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        qs = super().get_queryset().order_by("-year", "title")
        q      = self.request.GET.get("q", "")
        year   = self.request.GET.get("year", "")
        branch = self.request.GET.get("branch", "")
        ptype  = self.request.GET.get("type", "")
        if q:
            qs = qs.filter(models.Q(title__icontains=q) | models.Q(link__icontains=q))
        if year:
            qs = qs.filter(year=year)
        if branch:
            qs = qs.filter(branch=branch)
        if ptype:
            qs = qs.filter(project_type=ptype)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            "filter_q":      self.request.GET.get("q", ""),
            "filter_year":   self.request.GET.get("year", ""),
            "filter_branch": self.request.GET.get("branch", ""),
            "filter_type":   self.request.GET.get("type", ""),
            "all_years":     Project.objects.values_list("year", flat=True).distinct().order_by("-year"),
            "all_branches":  Project.objects.values_list("branch", flat=True).distinct(),
            "all_types":     Project.PROJECT_TYPES,
        })
        return ctx

class ProjectCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
     model = Project
     form_class = ProjectForm
     template_name = "projects/project_form.html"
     success_url = reverse_lazy("project_list")

class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"
    context_object_name = "project"

class ProjectUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
     model = Project
     form_class = ProjectForm
     template_name = "projects/project_form.html"
     success_url = reverse_lazy("project_list")