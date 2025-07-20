from django.urls import path
from .views import (
    ProjectListView,
    ProjectCreateView,
    ProjectDetailView,
    ProjectUpdateView,
)

urlpatterns = [
    path("", ProjectListView.as_view(), name="project_list"),
    path("add/", ProjectCreateView.as_view(), name="project_add"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
    path("<int:pk>/edit/", ProjectUpdateView.as_view(), name="project_edit"),
]
