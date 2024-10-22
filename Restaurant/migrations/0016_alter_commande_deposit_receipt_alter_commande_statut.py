# Generated by Django 5.1 on 2024-08-26 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0015_alter_commande_deposit_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='deposit_receipt',
            field=models.ImageField(upload_to='deposit_receipts/'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='statut',
            field=models.CharField(choices=[('en_attente', 'En attente'), ('livree', 'Livrée'), ('annulee', 'Annulee')], default='en_attente', max_length=20),
        ),
    ]
