# utilisateurs/views.py

from rest_framework import generics
from .models import Utilisateur
from ihmBack.serializers import UtilisateurSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication , SessionAuthentication , BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication



class UtilisateurListCreateView(generics.ListCreateAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

class UtilisateurRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]

class UserDetailsAPIView(APIView):
    authentication_classes = [ JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UtilisateurSerializer(user)  
        return Response(serializer.data)
