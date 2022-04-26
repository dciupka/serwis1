# Generated by Django 4.0.3 on 2022-04-26 19:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_geoposition_remove_geoinfo_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoinfo',
            name='list_size',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
