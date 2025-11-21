from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-placeholder'
DEBUG = True

# ✔ TU DOMINIO DE PYTHONANYWHERE
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'josebalanta.pythonanywhere.com']

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
        
        # ✔ Carpeta templates correcta
        'DIRS': [BASE_DIR / 'inmobiliaria' / 'templates'],
        
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'sitio.wsgi.application'

# ✔ Archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'inmobiliaria' / 'static']

# ✔ Carpetas necesarias para producción
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ✔ Para subir imágenes
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
