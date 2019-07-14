from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=40, verbose_name= "Nombre")
    fatherlastname = models.CharField(max_length=40, verbose_name="Apellido Paterno")
    motherlastname = models.CharField(max_length=40, verbose_name="Apellido Materno")
    sex = models.CharField(max_length=10, verbose_name="Genero HM-LGBTTTIQ")
    birthday = models.DateField(verbose_name="Cumpleaños", null=True, blank=True)
    email = models.EmailField(verbose_name="Correo Electrónico", null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name="Telefono", null=True, blank=True)
    work = models.CharField(max_length=40, verbose_name="Trabajo", null=True, blank=True)
    facebook = models.CharField(max_length=40, verbose_name="Facebook", null=True, blank=True)
    description = models.TextField(verbose_name= "Datos adicionales", null=True, blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="clients_files", null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")


    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
        ordering = ["-created"]

    def __str__(self):
        return self.name