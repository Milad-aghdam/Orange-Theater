from django.urls import path
from company import views

app_name = 'company'


urlpatterns = [
    path('foodhouse/', views.FoodhouseView.as_view(), name='foodhouse'),
    path('foodhouse/create/', views.FoodhouseCreateView.as_view(), name='foodhouse-create'),
    path('foodhouse/update/<int:pk>/', views.FoodhouseUpdateView.as_view(), name='foodhouse-update'),
    path('foodhouse/delete/<int:pk>/', views.FoodhouseDeleteView.as_view(), name='foodhouse-delete'),
    
    # Foodhub URLs
    path('foodhub/', views.FoodhubView.as_view(), name='foodhub'),
    path('foodhub/create/', views.FoodhubCreateView.as_view(), name='foodhub-create'),
    path('foodhub/update/<int:pk>/', views.FoodhubUpdateView.as_view(), name='foodhub-update'),
    path('foodhub/delete/<int:pk>/', views.FoodhubDeleteView.as_view(), name='foodhub-delete'),
]
