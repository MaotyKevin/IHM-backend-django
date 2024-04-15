# reservation/views.py

from rest_framework import generics , serializers , request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny  , IsAuthenticated 
from .models import Reservation
from ihmBack.serializers import ReservationSerializer , HostoriqueSerializer


class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class HistoriqueAPIView(APIView):


    def get(self, request, userID):
        reserv = Reservation.objects.filter(id=userID)
        serializer = HostoriqueSerializer(reserv, many=True)

        return Response(serializer.data)
     

     
    
    

