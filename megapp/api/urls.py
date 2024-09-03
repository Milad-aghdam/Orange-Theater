from django.urls import path
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('foothub/', views.FoothubApiView.as_view()),
    path('justeat/', views.JusteatApiView.as_view()),
    path('wtf/',views.WTFapiView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]






