from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve
from django.conf import settings

print(settings.DEBUG)
print(settings.SECRET_KEY)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core_apps.portfolio.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]
