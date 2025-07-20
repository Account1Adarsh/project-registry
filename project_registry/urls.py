# project_registry/urls.py

from django.contrib import admin
from django.urls import path, include     # ← include imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),   # ← just point at your app’s urls.py
]
