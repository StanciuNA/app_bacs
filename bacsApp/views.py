from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.template import loader
from django.shortcuts import render, redirect
from .models import *

def index(request):

    return render(request,"index.html")


def formulaire(request):
    bacs = Bac.objects.all()
    if request.method == 'POST':
        print(request.POST)
        site = Site.objects.get_or_create(adresse = request.POST["adresse"])
        retour = request.POST.get('retour',False)
        # user = Utilisateur.objects.filter(user = request.user)
        # livraison = Livraison.objects.create(site=site[0],
        #                       date=request.POST["dateLiv"],
        #                       retour=retour,
        #                       utilisateur = user[0])
        # for document in request.FILES.getlist('fichier'):
        #     doc = Document.objects.create(url = document)
        #     livraison.document.add(doc)    
        stock1 = Stock.objects.filter(site = site[0],bac=1)
        stock2 = Stock.objects.filter(site = site[0],bac=2)
        if len(stock1) == 0:
            if retour == "on":
                quantite = 0
                fournisseur = Site.objects.get(id = 1)
                stockFourn = Stock.objects.filter(site = fournisseur)
                stockFourn[0].quantite += int(request.POST["bac1"])
                stockFourn[0].quantite += int(request.POST["bac1"])
                #TODO update the stocks of the company that sent it 
                # investigate if you can reduce the code by using get_or_create function
            else:
                quantite = int(request.POST["Bac1"])
            stock1 = Stock(quantite = quantite,site = site[0],bac=bacs[0])
            stock1.save()
        else:
            stock1[0].quantite = stock1[0].quantite + int(request.POST["Bac1"])
            stock1[0].save()
        if len(stock2) == 0:
            if retour == "on":
                quantite = 0
            else:
                quantite = quantite = int(request.POST["Bac2"])
            stock2 = Stock(quantite = quantite,site = site[0],bac=bacs[1])
            stock2.save()
        else:
            stock2[0].quantite = stock2[0].quantite +int(request.POST["Bac2"])
            stock2[0].save()

    return render(request,"formulaire.html",{"bacs": bacs})

def login(request):
    if request.method == 'POST' :
        user = authenticate(request,username=request.POST["nom"], password=request.POST["mdp"])
        if user is not None:
            print(user)
            auth_login(request,user)
            return redirect("/")

    return render(request,"login.html")

def logout(request):
    user = auth_logout(request)

    return render(request,"index.html")

