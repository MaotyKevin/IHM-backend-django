# utilisateur/urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UtilisateurListCreateView , UtilisateurRetrieveUpdateDestroyView , MyTokenObtainPairView , UserDetailsAPIView

urlpatterns = [
  
    path('utilisateur/', UtilisateurListCreateView.as_view(), name='utilisateur-list-create'),
    path('utilisateur/<int:pk>/', UtilisateurRetrieveUpdateDestroyView.as_view(), name='utilisateur-detail'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Token generation
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh
    path('login/user-details/', UserDetailsAPIView.as_view(), name='user-details'),
]
