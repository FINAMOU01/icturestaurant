# Generated by Django 5.1 on 2024-08-26 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0014_alter_commande_deposit_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='deposit_receipt',
            field=models.FileField(default=False, upload_to='deposit_receipts/'),
            preserve_default=False,
        ),
    ]