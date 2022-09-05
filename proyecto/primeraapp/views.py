from django.shortcuts import render
from django.http import HttpResponse
import datetime



def vistaestructura(request):
    return HttpResponse("<h1>Hola denuevo<h1>")

def display(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Fecha y Hora Actual: </b>" + str(dt)
    return HttpResponse(s)

def renderTemplate(request):
    return render(request, 'index.html')