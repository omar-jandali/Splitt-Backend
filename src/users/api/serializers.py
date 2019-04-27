from rest_framework import serializers

from django.contrib.auth.models import User

from ..models import Profile, Detail, Friend


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'groups',
            'password'
        )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id',
            'user',
            'synapse',
            'bio',
            'profile_pic',
            'facebook',
            'twitter'
        )


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = (
            'id',
            'user',
            'gender',
            'phone',
            'street',
            'city',
            'state',
            'country',
            'zip_code'
        )

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = (
            'friender',
            'friended',
            'status',
            'blocked',
            'favorite',
        )
