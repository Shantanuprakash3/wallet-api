# Generated by Django 3.1.7 on 2021-03-26 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('walletapi', '0002_auto_20210326_1215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='walletId',
            new_name='wallet_id',
        ),
    ]
