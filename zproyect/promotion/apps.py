from django.apps import AppConfig


class PromotionConfig(AppConfig):
    name = 'promotion'
    # Por Default esta linea no viene se le agrega para cambiar el nombre de la APP
    # Podria estar en ingles y aqui lo cambiamos con el nombre que sea
    verbose_name = 'Promociones'