# medecin/views.py

from django.http import JsonResponse
from django.views import View
from rest_framework import generics , status , viewsets
from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Medecin , Grade , Specialization
from ihmBack.serializers import MedecinSerializer , GradeSerializer , SpelialiteSerializer , DISPOSerializer

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

class SGListCreateView(generics.ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpelialiteSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        
   
        new_specialization = {'id': response.data[-1]['id'] + 2, 'specialite': 'Generaliste'}

        response.data.append(new_specialization)
        
        return response
    

class MedecinAvailabilityView(View):
    
    def get(self, request, *args, **kwargs): 
        grade_or_specialization = request.data.get('grade')
        date_value = request.data.get('date')

        if not grade_or_specialization:
            return JsonResponse({'error': 'The query parameter "grade_or_specialization" is required.'}, status=400)
        if not date_value:
            return JsonResponse({'error': 'The query parameter "date_value" is required.'}, status=400)


        try:
            date_value = datetime.strptime(date_value, '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            return JsonResponse({'error': 'Invalid date_value format. Expected format: "YYYY-MM-DDTHH:MM:SS".'}, status=400)

        queryset = Medecin.objects.filter(
            grade__nomGrade=grade_or_specialization
        ) | Medecin.objects.filter(
            specialization__specialite=grade_or_specialization
        )

        queryset = queryset.filter(
            horairemedecin__horaireID__debut__gte=date_value
        ).distinct()

       
        serializer = DISPOSerializer(queryset, many=True)

        return JsonResponse(serializer.data, safe=False) 


    