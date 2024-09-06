from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .settings import DEBUG


urlpatterns = [
    path('admin/', admin.site.urls),
    # api urls
    path('api/', include('api.urls')),
    path('login/', include('accounts.urls')),
    path('', include('company.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
