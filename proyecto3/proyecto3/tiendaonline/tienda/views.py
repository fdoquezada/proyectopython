from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import datetime

def galeria(request):
    return HttpResponse("Hola, estás en la galería")

def despedida(request):
    return HttpResponse("hasta luego")

def calculeEdad(request,edad, agno):
    #edadActual=0
    perido=agno-1975
    edadFutura=edad+perido
    documento="<html><body><h2>Hola, en el año %s tendreas %s años" %(agno, edadFutura)
    return HttpResponse(documento)
    