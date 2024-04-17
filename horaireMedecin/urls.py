# reservation/urls.py

from django.urls import path
from .views import HoraireMedecinListCreateView , HoraireMedecinRetrieveUpdateDestroyView , Horaire_AND_HMCreateView , EDTAPIView

urlpatterns = [
 
    path('horaireMedecin/', HoraireMedecinListCreateView.as_view(), name='horaireMedecin-list-create'),
    path('horaireMedecin/<int:pk>/', HoraireMedecinRetrieveUpdateDestroyView.as_view(), name='horaireMedecin-detail'),

    path('Horaire&HM/', Horaire_AND_HMCreateView.as_view(), name='Horaire$HM'),

    path('EDT/', EDTAPIView.as_view(), name='EDT'),
]
