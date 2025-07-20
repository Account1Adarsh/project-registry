from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views   # ← add this import

urlpatterns = [
    path("admin/", admin.site.urls),

    # Authentication
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(next_page="project_list"),
        name="logout",
    ),

    # Your app
    path("", include("projects.urls")),
    # in root urls.py
    # path("accounts/logout/", auth_views.LogoutView.as_view(next_page="project_list"), name="logout"),

]
