# utilisateurs/views.py

from rest_framework import generics
from .models import Utilisateur
from ihmBack.serializers import UtilisateurSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny


class UtilisateurListCreateView(generics.ListCreateAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

class UtilisateurRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer



class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
