# Generated by Django 3.1.7 on 2021-03-26 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('walletapi', '0003_auto_20210326_1314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='wallet_id',
            new_name='wallet',
        ),
    ]
