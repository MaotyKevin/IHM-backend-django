# Generated by Django 5.0.2 on 2024-04-17 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horaire', '0003_remove_horaire_debaprem_remove_horaire_debmatin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horaire',
            name='jour',
        ),
    ]
