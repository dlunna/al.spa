# Generated by Django 2.2.3 on 2019-07-13 23:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20190713_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 13, 23, 52, 44, 193891, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]
