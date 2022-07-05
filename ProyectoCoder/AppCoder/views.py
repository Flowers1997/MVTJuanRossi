from django.shortcuts import render
from AppCoder.models import Familia
from django.http import HttpResponse

def familia(self):
    familia=Familia(nombre="Carlos", apellido="Rossi",edad=21,fechaDeNacimiento="2001-11-21",nombre2="Gerardo",apellido2="Rossi",edad2=22,fechaDeNacimiento2="2000-12-11",nombre3="Carla", apellido3="Rossi",edad3=23,fechaDeNacimiento3="1999-10-22")
    
    
    familia.save()
    texto= f"""Integrante agregado: nombre={familia.nombre}, apellido={familia.apellido}, edad={familia.edad}, Año de Nacimiento={familia.fechaDeNacimiento},                                    
    Integrante agregado: nombre={familia.nombre2}, apellido={familia.apellido2}, edad={familia.edad2}, Año de Nacimiento={familia.fechaDeNacimiento2},
    Integrante agregado: nombre={familia.nombre3}, apellido={familia.apellido3}, edad={familia.edad3}, Año de Nacimiento={familia.fechaDeNacimiento3}"""
    return HttpResponse(texto)



# Create your views here.
