# Generated by Django 2.2.4 on 2019-10-10 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='motherlastname',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Apellido Materno'),
        ),
        migrations.AlterField(
            model_name='client',
            name='sex',
            field=models.CharField(max_length=10, verbose_name='Genero Hombre - Mujer'),
        ),
        migrations.AlterField(
            model_name='client',
            name='workplace',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Lugar de trabajo'),
        ),
    ]