from django.urls import path
from company import views

app_name = 'company'
urlpatterns = [
    path('foodhouse/', views.FoodhouseView.as_view(), name='foodhouse'),
    path('foodhouse/create/', views.FoodhouseCreateView.as_view(), name='foodhouse-create'),
    path('foodhouse/update/<int:pk>/', views.FoodhouseUpdateView.as_view(), name='foodhouse-update'),
]
