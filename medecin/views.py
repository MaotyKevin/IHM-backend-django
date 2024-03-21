# medecin/views.py

from rest_framework import generics
from .models import Medecin
from ihmBack.serializers import MedecinSerializer


class MedecinListCreateView(generics.ListCreateAPIView):
    queryset = Medecin.objects.all()
    serializer_class = MedecinSerializer

class MedecinRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medecin.objects.all()
    serializer_class = MedecinSerializer