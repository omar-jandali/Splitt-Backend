from rest_framework import serializers

from ..models import Account, Transaction

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'user',
            'name',
            'bank',
            'type',
            'amount',
            'primary',
            'acct_ids'
        )
        depth=2

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'user_from',
            'user_to',
            'acct_from',
            'acct_to',
            'amount',
            'description'
        )
        depth=2
