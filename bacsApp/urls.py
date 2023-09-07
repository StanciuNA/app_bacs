from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("formulaire", views.formulaire, name="formulaire"),
    path("login", views.login, name="login"),
    path("logout",views.logout, name="logout"),
    path("liste",views.liste, name="liste")
]