# horaireMedecin/views.py

from rest_framework import generics , status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HoraireMedecin
from ihmBack.serializers import HoraireMedecinSerializer , HoraireSerializer


class HoraireMedecinListCreateView(generics.ListCreateAPIView):
    queryset = HoraireMedecin.objects.all()
    serializer_class = HoraireMedecinSerializer

class HoraireMedecinRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HoraireMedecin.objects.all()
    serializer_class = HoraireMedecinSerializer

class Horaire_AND_HMCreateView(APIView):
    def post(self, request, format=None):
        debut = request.data.get('debut')
        fin = request.data.get('fin')
        matricule = request.data.get('matricule')

        # Create a new entry in the Horaire table
        horaire_serializer = HoraireSerializer(data={'debut': debut, 'fin': fin})
        if horaire_serializer.is_valid():
            horaire = horaire_serializer.save()

            # Create a new entry in the HoraireMedecin table
            horaire_medecin_serializer = HoraireMedecinSerializer(data={'horaireID': horaire.pk, 'matricule': matricule})
            if horaire_medecin_serializer.is_valid():
                horaire_medecin_serializer.save()
                return Response(horaire_medecin_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(horaire_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
