from rest_framework import serializers

from ..models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = (
            'type',
            'user',
            'profile',
            'detail',
            'group',
            'member',
            'expense',
            'item',
            'account',
            'transaction',
            'description',
            'verified',
            'seen'
        )
