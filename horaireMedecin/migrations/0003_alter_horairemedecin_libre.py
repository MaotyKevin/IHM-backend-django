# Generated by Django 5.0.2 on 2024-05-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horaireMedecin', '0002_horairemedecin_libre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horairemedecin',
            name='libre',
            field=models.BooleanField(default=True),
        ),
    ]
