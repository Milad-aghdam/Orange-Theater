from django.urls import path
from company import views

app_name = 'company'


urlpatterns = [
    
    # Profile URLs
    path('', views.UserProfileView.as_view(), name='profile-all'),
    path('profile/update/<int:pk>/', views.UserUpdateView.as_view(), name='profile-update'),
    
    
    path('foodhouse/', views.FoodhouseView.as_view(), name='foodhouse'),
    path('foodhouse/create/', views.FoodhouseCreateView.as_view(), name='foodhouse-create'),
    path('foodhouse/update/<int:pk>/', views.FoodhouseUpdateView.as_view(), name='foodhouse-update'),
    path('foodhouse/delete/<int:pk>/', views.FoodhouseDeleteView.as_view(), name='foodhouse-delete'),
    
    # Foodhub URLs
    path('foodhub/', views.FoodhubView.as_view(), name='foodhub'),
    path('foodhub/create/', views.FoodhubCreateView.as_view(), name='foodhub-create'),
    path('foodhub/update/<int:pk>/', views.FoodhubUpdateView.as_view(), name='foodhub-update'),
    path('foodhub/delete/<int:pk>/', views.FoodhubDeleteView.as_view(), name='foodhub-delete'),
    
    # UberEats URLs
    path('ubereats/', views.UberEatsView.as_view(), name='ubereats'),
    path('ubereats/create/', views.UberEatsCreateView.as_view(), name='ubereats-create'),
    path('ubereats/update/<int:pk>/', views.UberEatsUpdateView.as_view(), name='ubereats-update'),
    path('ubereats/delete/<int:pk>/', views.UberEatsDeleteView.as_view(), name='ubereats-delete'),
    
    # Justeat URLs
    
    path('justeat/', views.JusteatView.as_view(), name='justeat'),
    path('justeat/create/', views.JusteatCreateView.as_view(), name='justeat-create'),
    path('justeat/update/<int:pk>/', views.JusteatUpdateView.as_view(), name='justeat-update'),
    path('justeat/delete/<int:pk>/', views.JusteatDeleteView.as_view(), name='justeat-delete'),
    
]
