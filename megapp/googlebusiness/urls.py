from django.urls import path
from . import views  

urlpatterns = [
    path('map-detail/', views.map_detail, name='map-detail'),
    path('edit/', views.edit_function, name='edit_function'),  
]