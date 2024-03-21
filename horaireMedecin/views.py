# horaireMedecin/views.py

from rest_framework import generics
from .models import HoraireMedecin
from ihmBack.serializers import HoraireMedecinSerializer


class HoraireMedecinListCreateView(generics.ListCreateAPIView):
    queryset = HoraireMedecin.objects.all()
    serializer_class = HoraireMedecinSerializer

class HoraireMedecinRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HoraireMedecin.objects.all()
    serializer_class = HoraireMedecinSerializer