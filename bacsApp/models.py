from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Utilisateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

class Bac(models.Model):
    libelle = models.CharField(max_length=30)

class Site(models.Model):
    libelle = models.CharField(max_length=30)
    furnisseur = models.BooleanField(max_length=30)
    bac = models.ManyToManyField(Bac,through="Stock")

class Documnet(models.Model):
    url = models.FileField(upload_to="")

class Livraison(models.Model):
    site = models.ForeignKey(Site, on_delete = models.SET_NULL, null= True)
    date = models.CharField(max_length=30)
    retour = models.CharField(max_length=30)
    utilisateur = models.ForeignKey(Utilisateur, on_delete = models.SET_NULL, null= True)
    livraison = models.ManyToManyField(Bac,through="Cargaison")
    document = models.ManyToManyField(Documnet)

class Cargaison(models.Model):
    bac = models.ForeignKey(Bac,on_delete=models.SET_NULL, null=True)
    livraison = models.ForeignKey(Livraison,on_delete=models.SET_NULL, null=True)
    quantite = models.PositiveIntegerField()
    

class Stock(models.Model):
    quantite = models.PositiveIntegerField()
    site = models.ForeignKey(Site,on_delete=models.SET_NULL, null=True)
    bac = models.ForeignKey(Bac,on_delete=models.SET_NULL, null=True)