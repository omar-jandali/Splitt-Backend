from ..models import Profile

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView

from ..serializers import ProfileSerializer


class UserListView(ListAPIView):
    queryset = Profile.objects.all()
    serializer = ProfileSerializer


class UserRetrieveView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer = ProfileSerializer


class UserCreaeteView(CreateAPIView):
    queryset = Profile.objects.all()
    serializer = ProfileSerializer


class UserDestroyView(DestroyAPIView):
    queryset = Profile.objects.all()
    serializer = ProfileSerializer


class UserUpdateView(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer = ProfileSerializer
