from users.models import Friend

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView

from users.api.serializers import FriendSerializer


class FriendListView(ListAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class FriendRetrieveView(RetrieveAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class FriendCreateView(CreateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class FriendDestroyView(DestroyAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class FriendUpdateView(UpdateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
