from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .settings import DEBUG
from home.views import ValidationSslView

urlpatterns = [
    # path('admin/', admin.site.urls),
    # api urls
    path('api/', include('api.urls')),
    path('account/', include('accounts.urls')),
    path('panel/', include('company.urls')),
    path('openhours/', include('googlebusiness.urls')),
    path('.well-known/pki-validation/31254999F419C5FD7B801C677268369D.txt', ValidationSslView.as_view(), name='validation'),
    path('', include('home.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
