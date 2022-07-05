from django.db import models

# Create your models here.


class Familia(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    edad= models.IntegerField(default=1)
    fechaDeNacimiento= models.DateField(default="2222-12-22")
    nombre2= models.CharField(max_length=30,default="aaa")
    apellido2= models.CharField(max_length=30, default="String")
    edad2= models.IntegerField(default=1)
    fechaDeNacimiento2= models.DateField(default="2222-12-22")
    nombre3= models.CharField(max_length=30,default="aaa")
    apellido3= models.CharField(max_length=30, default="String2")
    edad3= models.IntegerField(default=1)
    fechaDeNacimiento3= models.DateField(default="2222-12-22")



