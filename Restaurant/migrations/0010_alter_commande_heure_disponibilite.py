# Generated by Django 5.1 on 2024-08-24 22:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0009_remove_commande_mode_paiement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='heure_disponibilite',
            field=models.TimeField(default=datetime.time(22, 45, 17, 851385)),
        ),
    ]
