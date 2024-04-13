from django.db import models

class Medecin(models.Model):
    matricule = models.CharField(primary_key=True , max_length = 50)
    nom = models.CharField(max_length = 25)
    prenom = models.CharField(max_length = 25)
    specialite = models.CharField(max_length = 25)
    mail = models.EmailField(max_length=254, blank=True)
    cabinet = models.CharField(max_length = 25)
    Photo = models.ImageField(upload_to='medecin_photos/', null=True, blank=True) 
   
    def __str__(self):
        return f"{self.matricule} - {self.nom} {self.prenom}"