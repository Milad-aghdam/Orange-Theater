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


app_name = "api"






urlpatterns = [
    path('foodhub/', views.FoothubApiView.as_view()),
    path('justeat/', views.JusteatApiView.as_view()),
    path('foodhouse/', views.FoodhouseApiView.as_view()),
    path('whatthefork/',views.WsApiView.as_view()),
    path('ubereats/', views.UberEatsApiView.as_view()),
    path('mealzo/', views.MealzoApiView.as_view()),

    # google account api
    path('google-account/', views.AccountGoogleApiView.as_view()),
    path('businessinformation/', views.BusinessInformationApiView.as_view()),


    # jwt
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('schema/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]






