# Generated by Django 5.1 on 2024-09-10 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0031_alter_commande_date_commande_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='date_commande',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 10, 12, 37, 15, 274864)),
        ),
        migrations.AlterField(
            model_name='commande',
            name='heure_disponibilite',
            field=models.TimeField(default=datetime.time(19, 37, 15, 274864)),
        ),
    ]