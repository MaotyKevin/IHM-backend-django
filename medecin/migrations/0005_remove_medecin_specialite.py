# Generated by Django 5.0.2 on 2024-04-15 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medecin', '0004_medecin_tarif'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medecin',
            name='specialite',
        ),
    ]