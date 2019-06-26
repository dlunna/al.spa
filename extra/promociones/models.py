from django.db import models

# Create your models here.

# Dice que el nombre de la clase va en singular
# Por que el panel lo cambia a plural
class Project(models.Model):
    tittle = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField()
    #Añade automaticamente la Fecha de creacion
    created = models.DateTimeField(auto_now_add=True)
    #Añade la fecha de cuando de actualiza
    updated = models.DateTimeField(auto_now=True)