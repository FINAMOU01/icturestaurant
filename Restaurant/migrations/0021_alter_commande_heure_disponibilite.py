# Generated by Django 5.1 on 2024-08-30 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0020_alter_commande_date_commande_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='heure_disponibilite',
            field=models.TimeField(default=datetime.time(13, 0, 31, 339096)),
        ),
    ]
