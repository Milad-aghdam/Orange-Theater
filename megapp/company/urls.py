from django.urls import path
from company.views import HomeView

app_name = 'company'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
]