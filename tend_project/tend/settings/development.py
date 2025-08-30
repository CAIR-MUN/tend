"""
Development settings for Tend project.
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB', default='tend_db'),
        'USER': env('POSTGRES_USER', default='tend_user'),
        'PASSWORD': env('POSTGRES_PASSWORD', default='tend_password'),
        'HOST': env('POSTGRES_HOST', default='localhost'),
        'PORT': env('POSTGRES_PORT', default='5432'),
    }
}

# Add development-specific apps
INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

# Add debug toolbar middleware
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Debug toolbar configuration
INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

# Email backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Allow all origins for development
CORS_ALLOW_ALL_ORIGINS = True

# Disable HTTPS redirect in development
SECURE_SSL_REDIRECT = False

# Logging level
LOGGING['loggers']['tend']['level'] = 'DEBUG'
LOGGING['handlers']['console']['level'] = 'DEBUG'