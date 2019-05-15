from rest_framework import serializers

from ..models import Group, Member

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'id',
            'name',
            'description',
            'group_icon',
            'reference',
            'members',
            'host'
        )
        depth=2

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
            'id',
            'user',
            'group',
            'reference',
            'balance',
            'open_tabs'
        )
        depth=2
