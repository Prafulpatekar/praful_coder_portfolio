import logging

from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

logger = logging.getLogger('tuna')
logger.debug("Starting Debugger")
logger.info("Starting InfoLogger")
logger.warning("Starting WarningLogger")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myportfolio.core_apps.portfolio.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
