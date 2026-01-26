"""
Django settings for lexa project.
Django 4.2.x
"""

from pathlib import Path
import os
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "django-insecure-pz4*-(&2l@x+t-vnr^dv_y^pzj24^+3y@c1ykpe2dzsg-j!6=f")

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    "dashboard",
    "components",
    "extras",

    "crispy_forms",
    "crispy_bootstrap5",

    # Allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # Allauth
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "lexa.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",  # requerido por allauth
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "lexa.wsgi.application"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Argentina/Buenos_Aires"
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# STATIC_ROOT = BASE_DIR / "staticfiles"  # usar solo si haces collectstatic en prod

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Crispy
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Messages tags (Bootstrap alerts)
MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

# =========================
# EMAIL (DEV: no rompe login)
# =========================
# Con esto, Allauth "envía" emails a consola (terminal) y NO explota por from vacío.
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "no-reply@localhost")

# Si algún paquete usa SERVER_EMAIL:
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# =========================
# DJANGO-ALLAUTH
# =========================
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "account_login"
ACCOUNT_LOGOUT_ON_GET = False
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True

# Reemplazo deprecado: ACCOUNT_EMAIL_REQUIRED -> ACCOUNT_SIGNUP_FIELDS
# El * indica requerido
ACCOUNT_SIGNUP_FIELDS = ["email*", "username*", "password1*", "password2*"]

ACCOUNT_UNIQUE_EMAIL = True
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_LOGIN_ON_GET = True

# Para DEV: evitá que te bloquee el login por verificación obligatoria
# (si lo dejás en "mandatory", va a intentar enviar email sí o sí)
ACCOUNT_EMAIL_VERIFICATION = "none"   # <- clave para que no rompa
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

ACCOUNT_FORMS = {
    "login": "lexa.forms.UserLoginForm",
    "signup": "lexa.forms.UserRegistrationForm",
    "change_password": "lexa.forms.PasswordChangeForm",
    "set_password": "lexa.forms.PasswordSetForm",
    "reset_password": "lexa.forms.PasswordResetForm",
    "reset_password_from_key": "lexa.forms.PasswordResetKeyForm",
}

# Sites framework
# OJO: en sqlite nueva normalmente el Site es ID=1.
# Si dejás SITE_ID=3 y no existe, rompe flujos de allauth/socialaccount.
SITE_ID = int(os.environ.get("SITE_ID", "1"))

# Provider Configurations
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": ["profile", "email"],
        "AUTH_PARAMS": {"access_type": "online"},
    }
}
