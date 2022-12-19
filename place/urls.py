from django.urls import path
from .views import PlaceListCreateView,PlaceDetailView
urlpatterns = [
    path('',PlaceListCreateView.as_view(),name='place_list_create'),
    path('<int:pk>',PlaceDetailView.as_view(),name='place_detail'),

    
]