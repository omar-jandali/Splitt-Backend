from rest_framework import serializers

from ..models import Group, Member

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'name',
            'description',
            'group_icon',
            'reference',
            'members',
            'host'
        )

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
            'user',
            'group',
            'reference',
            'balance'
        )
