# Generated by Django 5.0.2 on 2024-04-15 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medecin', '0003_grade_specialization_medecin_grade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medecin',
            name='tarif',
            field=models.IntegerField(null=True),
        ),
    ]