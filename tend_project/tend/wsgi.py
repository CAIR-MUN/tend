"""
WSGI config for Tend project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tend.settings.production')

application = get_wsgi_application()