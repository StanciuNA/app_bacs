from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.template import loader
from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import redirect

def index(request):
    return render(request,"index.html")


def formulaire(request):
    bacs = Bac.objects.all()
    if request.method == 'POST':
        print(request.POST)
        site = Site.objects.get_or_create(adresse = request.POST["adresse"])
        retour = request.POST.get('retour',False)
        user = Utilisateur.objects.filter(user = request.user)
        livraison = Livraison.objects.create(site=site[0],
                              date=request.POST["dateLiv"],
                              retour=retour,
                              utilisateur = user[0])
        for document in request.FILES.getlist('fichier'):
            doc = Document.objects.create(url = document)
            livraison.document.add(doc)    
        stock1 = Stock.objects.get_or_create(site = site[0],bac=bacs[0])
        stock2 = Stock.objects.get_or_create(site = site[0],bac=bacs[1])
        fournisseur = Site.objects.get(id = 1)
        stockFournB1 = Stock.objects.get(site = fournisseur, bac=bacs[0])
        stockFournB2 = Stock.objects.get(site = fournisseur, bac=bacs[1])
        Cargaison.objects.create(livraison = livraison,bac = bacs[0],quantite = int(request.POST["Bac1"]))
        Cargaison.objects.create(livraison = livraison,bac = bacs[1],quantite = int(request.POST["Bac2"]))
        if retour == "on":
            stockFournB1.quantite = stockFournB1.quantite + int(request.POST["Bac1"])
            stockFournB1.save()
            stockFournB2.quantite = stockFournB2.quantite + int(request.POST["Bac2"])
            stockFournB2.save() 
            if stock1[0].quantite != 0: 
                stock1[0].quantite -= int(request.POST["Bac1"])
                stock1[0].save()
            if stock2[0].quantite != 0: 
                stock2[0].quantite -= int(request.POST["Bac2"])
                stock2[0].save()
        else:
            stockFournB1.quantite = stockFournB1.quantite - int(request.POST["Bac1"])
            stockFournB1.save()
            stockFournB2.quantite = stockFournB2.quantite - int(request.POST["Bac2"])
            stockFournB2.save() 
            stock1[0].quantite += int(request.POST["Bac1"])
            stock1[0].save()
            stock2[0].quantite += int(request.POST["Bac2"])
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
    auth_logout(request)
    return redirect("/")


def liste(request):
    user = request.user
    if(user.is_anonymous):
        print(request.user)
        return redirect("/login")
    else:
        if user.groups.filter(name='Responsables').exists(): 
            livraisons = Livraison.objects.all()
            for object in livraisons:
                object = object.cargaison_set.all()
                for a in object:
                    print(a.quantite)

        else:
            livraisons = Livraison.objects.filter(utilisateur=user)            
    return render(request,"liste.html",{"livraisons":livraisons})

