# medecin/views.py
import os
from rest_framework.permissions import IsAdminUser 
from django.http import JsonResponse
from django.views import View
from rest_framework import generics , status , viewsets
from rest_framework.permissions import AllowAny , IsAuthenticated
from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.files.storage import default_storage
from .models import Medecin , Grade , Specialization
from ihmBack.serializers import MedecinSerializer , GradeSerializer , SpelialiteSerializer , DISPOSerializer , PhotoMedecinSerializer

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
    

class PhotoMedecinAPIView(APIView):
    permission_classes = [IsAdminUser]  # Ensure user is admin

    def patch(self, request, *args, **kwargs):
        user = self.request.user

        # Check if the user is authenticated as an admin
        if user.is_authenticated and user.is_staff:
            serializer = PhotoMedecinSerializer(user, data=request.data)
            if serializer.is_valid():
                # Save the photo to the appropriate location
                photo = serializer.validated_data.get('Photo')
                if photo:
                    file_path = default_storage.save(os.path.join('medecin_photos', photo.name), photo)
                    user.Photo = file_path
                    user.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response("No photo provided", status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("User is not authorized", status=status.HTTP_403_FORBIDDEN)

    