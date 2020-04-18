"""Platzigram URL Module"""
#Django
from django.urls import path
from platzigram import view



urlpatterns = [
    path('hello-wordl/', view.hello_world), #la ruta hello-worl retorna la funcion
    path('hi/', view.hi),
]
