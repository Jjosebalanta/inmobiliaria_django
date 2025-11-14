"""Django settings for simple scaffold used for the assignment."""
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-placeholder'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'inmobiliaria',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
]
ROOT_URLCONF = 'sitio.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'inmobiliaria' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {'context_processors': []},
    },
]
WSGI_APPLICATION = 'sitio.wsgi.application'
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'inmobiliaria' / 'static']
