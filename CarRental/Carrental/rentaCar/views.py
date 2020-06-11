from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone

from .models import RentayDevolucion


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def devolver(request,id_renta):
    K:RentayDevolucion = RentayDevolucion.objects.get(id=id_renta)
    K.fecha_devolucion = timezone.now()
    K.estado = True
    K.vehiculo_rentayd.estado = True
    K.vehiculo_rentayd.save()
    K.save()
    return redirect('/rentaCar/rentaydevolucion/')