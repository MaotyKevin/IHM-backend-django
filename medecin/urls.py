# medecin/urls.py

from django.urls import path
from .views import MedecinListCreateView , MedecinRetrieveUpdateDestroyView

urlpatterns = [
  
    path('medecin/', MedecinListCreateView.as_view(), name='medecin-list-create'),
    path('medecin/<str:pk>/', MedecinRetrieveUpdateDestroyView.as_view(), name='medecin-detail'),

]
