# Generated by Django 2.2.4 on 2019-10-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=40, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('image', models.ImageField(upload_to='promotion_files', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'promocion',
                'verbose_name_plural': 'promociones',
                'ordering': ['-created'],
            },
        ),
    ]
