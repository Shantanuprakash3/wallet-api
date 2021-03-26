from django.db import models
import datetime

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70,blank=False, default='')
    phone = models.CharField(max_length=70,blank=False, default='')

class Wallet(models.Model):
    wallet_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=70, blank=False, default='')
    balance = models.FloatField(null=False, default=0.0)

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transactionTypes = [('Debit','Credit')]
    date = models.DateTimeField(default=datetime.datetime.now)
    transactionType = models.CharField(max_length=8, choices=transactionTypes)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.FloatField(null=False, default=0.0)