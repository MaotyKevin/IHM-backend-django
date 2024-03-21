from django.db import models
from medecin.models import Medecin

class Horaire(models.Model):
    horaireID = models.AutoField(primary_key=True)
    debMatin = models.CharField(max_length = 5)
    finMatin = models.CharField(max_length = 5)
    debAprem = models.CharField(max_length = 5)
    finAprem = models.CharField(max_length = 5)


   
    def __str__(self):
        return f"Matin : {self.debMatin}-{self.finMatin} , Aprem : {self.debAprem}-{self.finAprem}"