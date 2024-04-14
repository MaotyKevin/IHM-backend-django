# medecin/views.py

from rest_framework import generics , status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Medecin , Grade , Specialization
from ihmBack.serializers import MedecinSerializer , GradeSerializer , SpelialiteSerializer 

class GradeListCreateView(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class GradeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class SpecialisteListCreateView(generics.ListCreateAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpelialiteSerializer

class SpecialisteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpelialiteSerializer

class MedecinListCreateView(generics.ListCreateAPIView):
    queryset = Medecin.objects.all()
    serializer_class = MedecinSerializer

class MedecinRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medecin.objects.all()
    serializer_class = MedecinSerializer

class SGListCreateView(generics.ListCreateAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpelialiteSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        
   
        new_specialization = {'id': response.data[-1]['id'] + 1, 'specialite': 'Generaliste'}

        response.data.append(new_specialization)
        
        return response