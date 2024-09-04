from django.urls import path
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularRedocView,
    SpectacularSwaggerView,
    SpectacularAPIView,
)

from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('foothub/', views.FoothubApiView.as_view()),
    path('justeat/', views.JusteatApiView.as_view()),
    path('wtf/',views.WTFapiView.as_view()),
    path('ubereats/', views.UberEatsApiView.as_view()),




    # jwt
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('schema/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]






