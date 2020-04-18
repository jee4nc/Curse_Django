"""Platzigram Views"""

#Django
from django.http import HttpResponse

#Utilidades
from datetime import datetime



def hello_world(request):   # funcion que recibe un request como parametro
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    #datetime.now trae la hora de ahora
    #srtime setea la hora en un formato

      #Devuelve una instancia de httpResponse
    return HttpResponse('Oh hi! current server time is {now}'.format
    (now=now))
    # {} sirve para concadenar en python y se setea formato

def hi(request):
    import pdb; pdb.set_trace()
    return HttpResponse('Hi!')