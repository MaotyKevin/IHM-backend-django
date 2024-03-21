# reservation/urls.py

from django.urls import path
from .views import HoraireMedecinListCreateView , HoraireMedecinRetrieveUpdateDestroyView

urlpatterns = [
 
    path('horaireMedecin/', HoraireMedecinListCreateView.as_view(), name='horaireMedecin-list-create'),
    path('horaireMedecin/<int:pk>/', HoraireMedecinRetrieveUpdateDestroyView.as_view(), name='horaireMedecin-detail'),

]
