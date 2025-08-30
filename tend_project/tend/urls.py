"""
URL configuration for Tend project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # PWA
    path('', include('pwa.urls')),
    
    # Core app (will handle home page and main functionality)
    path('', include('apps.core.urls')),
    
    # User management
    path('auth/', include('apps.users.urls')),
    
    # API endpoints (for future use)
    path('api/v1/', include('apps.api.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    # Debug toolbar
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns