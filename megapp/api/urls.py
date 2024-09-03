from django.urls import path
from api import views


urlpatterns = [
    path('foothub/', views.FoothubApiView.as_view()),
]

