"""Platzigram Views"""

#Django
from django.http import HttpResponse

#Utilidades
from datetime import datetime
import json


def hello_world(request):   # funcion que recibe un request como parametro
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    #datetime.now trae la hora de ahora
    #srtime setea la hora en un formato

      #Devuelve una instancia de httpResponse
    return HttpResponse('Oh hi! current server time is {now}'.format
    (now=now))
    # {} sirve para concadenar en python y se setea formato

def sortedNumbers(request):
  #ordena los numeros con sorted

    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_inst = sorted(numbers)
    data = {
      'status': 'ok',
      'numbers': sorted_inst,
      'message': 'Intergers sorted succesfully'
    }
    return HttpResponse(json.dumps(data, indent=4),
     content_type='application/json')

def sayHi(request, name, age):
  #Return a greeting

  if age < 14:
    message = 'Sorry {}, you are not allowed here'.format(name) #{} y al final .format(name) setea el valor
  else:
    message = 'Hello {}!, Welcome to Platzigram'.format(name)
  return HttpResponse(message)