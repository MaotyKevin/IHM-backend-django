# Generated by Django 5.0.2 on 2024-04-17 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horaire', '0004_remove_horaire_jour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horaire',
            name='debut',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='horaire',
            name='fin',
            field=models.DateTimeField(null=True),
        ),
    ]
