# Generated by Django 4.0.3 on 2022-04-10 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_geoinfo_iata_airport_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoinfo',
            name='iata_airport_code',
            field=models.BooleanField(null=True),
        ),
    ]
