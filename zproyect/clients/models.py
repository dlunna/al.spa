from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=40, verbose_name= "Nombre")
    fatherlastname = models.CharField(max_length=40, verbose_name="Apellido Paterno")
    motherlastname = models.CharField(max_length=40, verbose_name="Apellido Materno", null=True, blank=True)
    sex = models.CharField(max_length=10, verbose_name="Genero Hombre - Mujer")
    birthday = models.DateField(verbose_name="Cumpleaños", null=True, blank=True)
    email = models.EmailField(verbose_name="Correo Electrónico", null=True, blank=True)
    celphone = models.CharField(max_length=20, verbose_name="Número celular", null=True, blank=True)
    workplace = models.CharField(max_length=40, verbose_name="Lugar de trabajo", null=True, blank=True)
    workphone = models.CharField(max_length=40, verbose_name="Número de telefono del trabajo", null=True, blank=True)
    facebook = models.CharField(max_length=40, verbose_name="Facebook", null=True, blank=True)
    instagram = models.CharField(max_length=40, verbose_name="Instagram", null=True, blank=True)
    description = RichTextField(verbose_name="Datos adicionales", null=True, blank=True)
    photo = models.ImageField(verbose_name="Foto", upload_to="clients_files", null=True, blank=True)
    sign = models.ImageField(verbose_name="Firma responsiva", upload_to="clients_files", null=True, blank=True)
    assessment = models.ImageField(verbose_name="Valoración", upload_to="clients_files", null=True, blank=True)
    packsheet = models.ImageField(verbose_name="Hoja de paquete", upload_to="clients_files", null=True, blank=True)
    consent = models.ImageField(verbose_name="Consentimiento informado", upload_to="clients_files", null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")


    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
        ordering = ["-created"]



    def __str__(self):
        return self.name