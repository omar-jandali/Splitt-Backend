from rest_framework import serializers

from django.contrib.auth.models import User

from ..models import Profile, Detail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
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
            'user',
            'gender',
            'phone',
            'street',
            'city',
            'state',
            'country',
            'zip_code'
        )