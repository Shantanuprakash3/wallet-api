from rest_framework import serializers 
from walletapi.models import Wallet
from walletapi.models import Transaction
 
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('wallet_id',
                  'user_id',
                  'balance')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id',
                    'date',
                    'transactionType',
                    'walletId',
                    'amount')