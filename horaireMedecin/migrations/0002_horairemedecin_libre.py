# Generated by Django 5.0.2 on 2024-04-17 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horaireMedecin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='horairemedecin',
            name='libre',
            field=models.BooleanField(default=False),
        ),
    ]