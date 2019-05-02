from rest_framework import serializers

from ..models import Expense, Item

class ExpensesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = (
            'group',
            'user',
            'location',
            'split',
            'total',
            'tax',
            'tip',
            'reference'
        )

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'expense',
            'user',
            'requested',
            'description',
            'amount',
            'paid',
            'verified',
            'reference'
        )
