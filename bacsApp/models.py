from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Utilisateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    nom = models.CharField(max_length=30,null=True)
    mdp = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.nom
    

class Bac(models.Model):
    libelle = models.CharField(max_length=30)
    objects = models.Manager()
    
    def __str__(self):
        return self.libelle

class Site(models.Model):
    adresse = models.CharField(max_length=30,null=True)
    bac = models.ManyToManyField(Bac,through="Stock")
    objects = models.Manager()

    def __str__(self):
        return self.adresse

class Document(models.Model):
    url = models.FileField(upload_to="",null=True)
    objects = models.Manager()

    def __str__(self):
        return self.url

class Livraison(models.Model):
    site = models.ForeignKey(Site, on_delete = models.SET_NULL, null= True)
    date = models.CharField(max_length=30)
    retour = models.CharField(max_length=30,default=False)
    utilisateur = models.ForeignKey(Utilisateur, on_delete = models.SET_NULL, null= True)
    une_cargaison = models.ManyToManyField(Bac,through="Cargaison")
    document = models.ManyToManyField(Document)
    objects = models.Manager()

class Cargaison(models.Model):
    bac = models.ForeignKey(Bac,on_delete=models.SET_NULL, null=True)
    livraison = models.ForeignKey(Livraison,on_delete=models.SET_NULL, null=True)
    quantite = models.PositiveIntegerField()
    objects = models.Manager()

class Stock(models.Model):
    quantite = models.PositiveIntegerField(default=0)
    site = models.ForeignKey(Site,on_delete=models.SET_NULL, null=True)
    bac = models.ForeignKey(Bac,on_delete=models.SET_NULL, null=True)
    objects = models.Manager()