from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),

    # api urls
    path('api/', include('api.urls')),
    # path('', include('company.urls')),


]
