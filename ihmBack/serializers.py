# poste/serializers.py

from rest_framework import serializers
from horaire.models import Horaire
from medecin.models import Medecin , Grade , Specialization
from utilisateur.models import Utilisateur
from reservation.models import Reservation
from horaireMedecin.models import HoraireMedecin

class GradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = '__all__'

class SpelialiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialization
        fields = '__all__'

class MedecinSerializer(serializers.ModelSerializer):
    Grade = GradeSerializer(source='id', read_only=True)
    Specialization = SpelialiteSerializer(source='id', read_only=True)
    class Meta:
        model = Medecin
        fields = '__all__'
        extra_kwargs = {'Photo': {'required': False}}

class HoraireSerializer(serializers.ModelSerializer):

    class Meta:
        model = Horaire
        fields = '__all__'


class UtilisateurSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=False)

    class Meta:
        model = Utilisateur
        fields = ['id', 'username', 'email', 'first_name' , 'last_name' , 'contact' , 'password' , 'UserPhoto']
        extra_kwargs = {'UserPhoto': {'required': False}}


    def create(self, validated_data):
        password = validated_data.pop('password')
        account = Utilisateur.objects.create(**validated_data)
        account.set_password(password)
        account.save()
        return account

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class ReservationSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(source='id', read_only=True)
    medecin = MedecinSerializer(source='matricule', read_only=True)

    class Meta:
        model = Reservation
        fields = '__all__'

class HoraireMedecinSerializer(serializers.ModelSerializer):
    horaire = HoraireSerializer(source='horaireID', read_only=True)
    medecin = MedecinSerializer(source='matricule', read_only=True)

    class Meta:
        model = HoraireMedecin
        fields = '__all__'






      