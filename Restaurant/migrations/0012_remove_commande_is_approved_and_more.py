# Generated by Django 5.1 on 2024-08-25 23:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0011_commande_is_approved_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='is_approved',
        ),
        migrations.AlterField(
            model_name='commande',
            name='heure_disponibilite',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
