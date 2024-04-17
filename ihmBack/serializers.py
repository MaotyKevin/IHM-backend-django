# poste/serializers.py

from rest_framework import serializers
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
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
    password = serializers.CharField(write_only=True , required=False)

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
        UserPhoto = validated_data.pop('UserPhoto', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    
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

class HostoriqueSerializer(serializers.ModelSerializer):

    doctor_name = serializers.CharField(source='matricule.nom')
    image_doc = serializers.CharField(source='matricule.Photo')
    dateHeure = serializers.DateTimeField()
    gradeDoc = serializers.CharField(source='matricule.grade')
    cabinet = serializers.CharField(source='matricule.cabinet')
    

    class Meta:
        model = Reservation
        fields = ['doctor_name', 'image_doc', 'dateHeure' , 'gradeDoc' , 'cabinet']

class UserWithReservationSerializer(serializers.ModelSerializer):
    most_recent_reservation = serializers.SerializerMethodField()

    class Meta:
        model = Utilisateur
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'contact', 'UserPhoto', 'most_recent_reservation']

    def get_most_recent_reservation(self, obj):
        try:
            most_recent_reservation = obj.reservation_set.latest('dateHeure').dateHeure
        except ObjectDoesNotExist:
            most_recent_reservation = None
        return most_recent_reservation
    
class EDTSerializer(serializers.ModelSerializer):
    matricule = serializers.StringRelatedField(source='matricule.matricule')
    username = serializers.SerializerMethodField()
    debut = serializers.DateTimeField(source='horaireID.debut')
    fin = serializers.DateTimeField(source='horaireID.fin')

    class Meta:
        model = HoraireMedecin
        fields = ['HoraireMedecinID', 'matricule', 'libre', 'username', 'debut', 'fin']

    def get_username(self, obj):
        try:
            reservation = Reservation.objects.get(matricule=obj.matricule)
            return reservation.id.username
        except Reservation.DoesNotExist:
            return None
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['debut'] = instance.horaireID.debut  # Assuming debut is already a datetime object
        return representation
        
def group_by_week(data):
    grouped_data = {}
    for entry in data:
        debut = entry['debut']
        print(type(debut))
        if debut:
            debut_week = debut.isocalendar()[1]
            if debut_week not in grouped_data:
                grouped_data[debut_week] = []
            grouped_data[debut_week].append(entry)
    return grouped_data



    













      