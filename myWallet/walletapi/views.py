from django.shortcuts import render
import json
import traceback
import sys

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from walletapi.models import Wallet
from walletapi.models import Transaction
from walletapi.serializers import WalletSerializer
from walletapi.serializers import TransactionSerializer
from rest_framework.decorators import api_view
from django.conf import settings
from django.db import transaction
from django.db.utils import OperationalError


@api_view(['GET', 'POST', 'DELETE'])
def wallet(request):
    # CRUD for wallet

    ## create wallet
    # expects user_id, starting balance and wallet name
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        try:
            user_id = str(body['user_id'])
            name = str(body['name'])
            balance = float(body['balance'])
            response = Wallet.objects.create(name=name, user_id=user_id, balance=balance)
            response.save()
            return JsonResponse({"created": response.wallet_id}, safe=False)
        except:
            return JsonResponse({"error": "not a valid data"}, safe=False)

def wallet_balance(request, pk):
    ## GET balance
    # expects wallet_id
    wallet = Wallet.objects.get(pk=pk)
    if request.method == 'GET': 
        tutorial_serializer = WalletSerializer(wallet) 
        return JsonResponse(tutorial_serializer.data)    

@api_view(['POST'])
@transaction.atomic
def transaction_credit(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        try:
            wallet_id = str(body['wallet_id'])
            amount = float(body['amount'])
            # get wallet balance
            wallet_data = Wallet.objects.get(wallet_id=wallet_id)
            wallet_balance = float(wallet_data.balance) 

            # check for upper limit?
            new_balance = wallet_balance + amount
            print(new_balance)
            
            wallet = Wallet.objects.filter(wallet_id=wallet_id).update(balance=new_balance)
    
            # add transaction record
            response = Transaction.objects.create(transactionType='Credit', wallet_id=wallet_id, amount=amount)
            response.save()
        
            return JsonResponse({"updated": new_balance}, safe=False)
        except OperationalError as e:
            return JsonResponse({"error" : "Error processing parallel transaction, retry"}, status=429 ,safe=False)
            pass
        except:
            print(traceback.print_exc())
            return JsonResponse({"error": "not a valid data"}, safe=False)

@api_view(['POST'])
@transaction.atomic
def transaction_debit(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        try:
            wallet_id = str(body['wallet_id'])
            amount = float(body['amount'])
            # deduct from wallet balance
            # get wallet balance
            wallet_data = Wallet.objects.get(wallet_id=wallet_id)
            wallet_balance = float(wallet_data.balance) 

            # check for upper limit?
            if wallet_balance - amount < settings.MIN_BALANCE:
                return JsonResponse({"error": "Min balance can't be less than 0.0"}, safe=False)
            else:
                new_balance = wallet_balance - amount

            wallet = Wallet.objects.filter(wallet_id=wallet_id).update(balance=new_balance)
    
            # add transaction record
            response = Transaction.objects.create(transactionType='Debit', wallet_id=wallet_id, amount=amount)
            response.save()
        
            return JsonResponse({"updated": new_balance}, safe=False)
        except OperationalError:
            return JsonResponse({"error" : "Error processing parallel transaction, retry"}, status=429,safe=False)
            pass
        except:
            return JsonResponse({"error": "not a valid data"}, safe=False)