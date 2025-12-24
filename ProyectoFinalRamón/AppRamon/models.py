from django.db import models

class Competencia(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to='competencias/', blank=True, null=True)

    def __str__(self):
        return self.nombre


class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    posición = models.CharField(max_length=30)
    equipo = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='jugadores/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Manager(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    equipo = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='managers/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Equipo(models.Model):
    nombre = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='equipos/', blank=True, null=True)

    def __str__(self):
        return self.nombre