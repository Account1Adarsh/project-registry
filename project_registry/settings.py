import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = "replace-me-with-a-secure-key"
# DEBUG = True
# ALLOWED_HOSTS = []

LOGGING = {
  "version": 1,
  "handlers": {"console": {"class":"logging.StreamHandler"}},
  "loggers": {
    "django.request": {"handlers":["console"], "level":"DEBUG", "propagate": True},
  },
}

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "widget_tweaks",
    "projects",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = "project_registry.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [ BASE_DIR / "templates" ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project_registry.wsgi.application"
ASGI_APPLICATION = "project_registry.asgi.application"

import dj_database_url, os

DATABASES = {
  'default': dj_database_url.config(
      default='sqlite:///db.sqlite3',
      conn_max_age=600,
      ssl_require=True
  )
}


LOGIN_REDIRECT_URL = 'project_list'     # or you can use '/'  

# Where to redirect after logout
LOGOUT_REDIRECT_URL = 'project_list'    # or '/'  

AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [ BASE_DIR / "static" ]
# … earlier settings …

# Remove this hard‑coded key:
# SECRET_KEY = "replace-me-with-a-secure-key"

# Instead, read it from the ENV:
SECRET_KEY = os.environ['SECRET_KEY']

# DEBUG flag from the ENV (default to False)
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Allow Render’s hostname + localhost
ALLOWED_HOSTS = [
    os.environ.get('RENDER_EXTERNAL_HOSTNAME'),
    'localhost',
]
