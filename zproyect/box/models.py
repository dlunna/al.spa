from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from clients.models import Client
#from djmoney.models.fields import MoneyField

# Create your models here.

class Venta(models.Model):
    #key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True, default='Venta')
    content = models.TextField(verbose_name="Descripción de la venta")
    cost = models.FloatField(verbose_name="Costo", default=0)
    #kost = MoneyField(
    #    max_digits=19,
    #    decimal_places=2,
    #    default=0,
    #    default_currency='USD')
    salesdate = models.DateTimeField(verbose_name="Fecha de la venta", default=now)
    salesmen = models.ForeignKey (User, verbose_name="vendedor", on_delete=models.CASCADE)
    client = models.ForeignKey(Client, verbose_name="cliente", on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")


    class Meta:
        verbose_name = "venta"
        verbose_name_plural = "ventas"
        ordering = ["-created"]

    def __str__(self):
        return self.content
