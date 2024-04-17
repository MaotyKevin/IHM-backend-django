# utilisateurs/views.py

from rest_framework import generics, viewsets , status
from django.contrib.auth.hashers import check_password
from .models import Utilisateur
from ihmBack.serializers import UtilisateurSerializer , ChangePasswordSerializer
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
    
class ChangePasswordViewSet(viewsets.ViewSet):
    authentication_classes = [ JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def change_password(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        old_password = serializer.validated_data['old_password']
        new_password = serializer.validated_data['new_password']
        #confirm_password = serializer.validated_data['confirm_password']

        # Check if old password matches
        if not check_password(old_password, user.password):
            return Response({'error': 'Invalid old password'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if new password matches the confirmation
        #if new_password != confirm_password:
            #return Response({'error': 'New password and confirm password do not match'}, status=status.HTTP_400_BAD_REQUEST)

        # Set the new password
        user.set_password(new_password)
        user.save()

        return Response({'success': 'Password changed successfully'}, status=status.HTTP_200_OK)
