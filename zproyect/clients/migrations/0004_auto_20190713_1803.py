# Generated by Django 2.2.3 on 2019-07-13 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20190713_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='clients_files', verbose_name='Imagen'),
        ),
    ]