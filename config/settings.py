import os
from pathlib import Path
import dj_database_url


# ============================================================
# BASE DIR
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# CHARGEMENT DU FICHIER .env
# ============================================================

def _load_env():
    env_file = BASE_DIR / ".env"

    if not env_file.exists():
        return

    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()

        if not line or line.startswith("#") or "=" not in line:
            continue

        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")

        os.environ.setdefault(key, value)


_load_env()


# ============================================================
# VARIABLES D'ENVIRONNEMENT
# ============================================================

def env_str(key, default=""):
    return os.environ.get(key, default)


def env_bool(key, default=False):
    return os.environ.get(
        key,
        str(default)
    ).strip().lower() in ("1", "true", "yes", "on")


# ============================================================
# SECURITY
# ============================================================

SECRET_KEY = env_str(
    "SECRET_KEY",
    "django-insecure-dev-only-change-me"
)

DEBUG = env_bool("DEBUG", False)

ALLOWED_HOSTS = [
    h.strip()
    for h in env_str(
        "ALLOWED_HOSTS",
        "localhost,127.0.0.1"
    ).split(",")
    if h.strip()
]


# ============================================================
# APPLICATIONS
# ============================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
    'blog',
    'contact',
    'cloudinary_storage',
    'cloudinary',
]


# ============================================================
# MIDDLEWARE
# ============================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ============================================================
# URL / WSGI
# ============================================================

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"


# ============================================================
# TEMPLATES
# ============================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates"
        ],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ============================================================
# DATABASE
# ============================================================

DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + str(BASE_DIR / "db.sqlite3"),
        conn_max_age=600,
        ssl_require=False,
    )
}


# ============================================================
# PASSWORD VALIDATION
# ============================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME":
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME":
            "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME":
            "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME":
            "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ============================================================
# INTERNATIONALIZATION
# ============================================================

LANGUAGE_CODE = "fr-FR"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# ============================================================
# STATIC FILES
# ============================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"


# ============================================================
# MEDIA FILES
# ============================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# ============================================================
# EMAIL — BREVO SMTP
# ============================================================

EMAIL_BACKEND = env_str(
    "EMAIL_BACKEND",
    "django.core.mail.backends.smtp.EmailBackend"
)

EMAIL_HOST = env_str(
    "EMAIL_HOST",
    "smtp-relay.brevo.com"
)

EMAIL_PORT = int(
    env_str("EMAIL_PORT", "587")
)

EMAIL_USE_TLS = env_bool(
    "EMAIL_USE_TLS",
    True
)

EMAIL_HOST_USER = env_str(
    "EMAIL_HOST_USER",
    ""
)

EMAIL_HOST_PASSWORD = env_str(
    "EMAIL_HOST_PASSWORD",
    ""
)

DEFAULT_FROM_EMAIL = env_str(
    "DEFAULT_FROM_EMAIL",
    EMAIL_HOST_USER
)

CONTACT_RECIPIENT = env_str(
    "EMAIL_RECIPIENT",
    EMAIL_HOST_USER
)


# ============================================================
# CLOUDINARY (stockage des images uploadées)
# ============================================================
#
# En production, les images doivent être stockées sur Cloudinary :
# le disque de Render (offre gratuite) est éphémère et efface les
# fichiers uploadés au moindre redémarrage.
#
# Les 3 identifiants sont lus dans l'environnement. S'ils sont tous
# présents on utilise Cloudinary, sinon on retombe sur le stockage
# local (pratique en développement).

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env_str('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': env_str('CLOUDINARY_API_KEY'),
    'API_SECRET': env_str('CLOUDINARY_API_SECRET'),
}

USE_CLOUDINARY = all(CLOUDINARY_STORAGE.values())

if USE_CLOUDINARY:
    DEFAULT_STORAGE_BACKEND = (
        "cloudinary_storage.storage.MediaCloudinaryStorage"
    )
else:
    DEFAULT_STORAGE_BACKEND = (
        "django.core.files.storage.FileSystemStorage"
    )


# ============================================================
# STORAGE (Django >= 4.2)
# ============================================================

STORAGES = {
    "default": {
        "BACKEND": DEFAULT_STORAGE_BACKEND,
    },
    "staticfiles": {
        "BACKEND": (
            "whitenoise.storage.CompressedManifestStaticFilesStorage"
        ),
    },
}


# ============================================================
# SÉCURITÉ PRODUCTION
# ============================================================

if not DEBUG:

    SECURE_SSL_REDIRECT = True

    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True

    SECURE_HSTS_SECONDS = 31536000

    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    SECURE_HSTS_PRELOAD = True

    SECURE_PROXY_SSL_HEADER = (
        "HTTP_X_FORWARDED_PROTO",
        "https"
    )