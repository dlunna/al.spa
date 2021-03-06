# Generated by Django 2.2.4 on 2019-10-09 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(default='Venta', max_length=100, unique=True, verbose_name='Nombre clave')),
                ('content', models.TextField(verbose_name='Descripción de la venta')),
                ('cost', models.FloatField(default=0, verbose_name='Costo')),
                ('salesdate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de la venta')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client', verbose_name='cliente')),
                ('salesmen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='vendedor')),
            ],
            options={
                'verbose_name': 'venta',
                'verbose_name_plural': 'ventas',
                'ordering': ['-created'],
            },
        ),
    ]
