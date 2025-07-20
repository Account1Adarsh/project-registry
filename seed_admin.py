#!/usr/bin/env python
import os
import django
from django.contrib.auth import get_user_model

# Point Django at your settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_registry.settings")
django.setup()

User = get_user_model()

# Change these to whatever credentials you want in prod
ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
ADMIN_EMAIL    = os.environ.get("ADMIN_EMAIL",    "admin@example.com")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "changeme")

if not User.objects.filter(username=ADMIN_USERNAME).exists():
    print(f"Creating superuser '{ADMIN_USERNAME}'")
    User.objects.create_superuser(
        ADMIN_USERNAME,
        ADMIN_EMAIL,
        ADMIN_PASSWORD
    )
else:
    print(f"Superuser '{ADMIN_USERNAME}' already exists")
