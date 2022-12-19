from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
from .models import Place
from .serializers import PlaceSerializer
from .permissions import AdministratorOnly

class PlaceListCreateView(ListCreateAPIView):
    
    queryset=Place.objects.all()
    serializer_class=PlaceSerializer

class PlaceDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Place.objects.all()
    serializer_class=PlaceSerializer
    permission_classes=[AdministratorOnly]