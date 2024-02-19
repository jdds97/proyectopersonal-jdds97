from django.db import models


class TipoEntrenamiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return str(self.nombre)


class GrupoMuscular(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre)


class Ejercicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    grupos_musculares = models.ManyToManyField(GrupoMuscular)

    def __str__(self):
        return str(self.nombre)


class Rutina(models.Model):
    fecha = models.DateField()
    tipo_entrenamiento = models.ForeignKey(TipoEntrenamiento, on_delete=models.CASCADE)
    ejercicios = models.ManyToManyField(Ejercicio)

    def __str__(self):
        return f"Rutina - {self.fecha} "
