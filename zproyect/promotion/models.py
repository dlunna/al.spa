from django.db import models

# Create your models here.

# Dice que el nombre de la clase va en singular
# Por que el panel lo cambia a plural
class Project(models.Model):
    # se agrega el verbose name para cambiar el nombre a español en el panel de admon
    tittle = models.CharField(max_length=40, verbose_name= "Título")
    description = models.TextField(verbose_name= "Descripción")
    # ORIGINAL image = models.ImageField(verbose_name="Imagen")
    # se agrega upload_to XXXX para colocar las imagenes dentro de una carpeta
    image = models.ImageField(verbose_name="Imagen", upload_to="promotion_files")
    # Campo opcional para agregar una URL
    #link = models.URLField(verbose_name="URL", null=True, blank=True)
    # Campo para el costo
    #cost = models.DecimalField(verbose_name="Costo", max_digits=10, decimal_places=2, default=0)

    #Añade automaticamente la Fecha de creacion
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    #Añade la fecha de cuando de actualiza
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")


    class Meta:
        #Nombre para singular de la clase
        verbose_name = "promocion"
        #Nombre para plural de la clase
        verbose_name_plural = "promociones"
        # Ordena los proyectos desde el ultimo creado
        ordering = ["-created"]

    #Esta redefiniendo la cadena string
    #Esto sirve para mostrar el nombre del Titulo que se esta guardando en la BD
    def __str__(self):
        return self.tittle