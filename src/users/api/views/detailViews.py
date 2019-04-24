from users.models import Detail

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView

from ..serializers import DetailSerializer


class UserListView(ListAPIView):
    queryset = Detail.objects.all()
    serializer = DetailSerializer


class UserRetrieveView(RetrieveAPIView):
    queryset = Detail.objects.all()
    serializer = DetailSerializer


class UserCreaeteView(CreateAPIView):
    queryset = Detail.objects.all()
    serializer = DetailSerializer


class UserDestroyView(DestroyAPIView):
    queryset = Detail.objects.all()
    serializer = DetailSerializer


class UserUpdateView(UpdateAPIView):
    queryset = Detail.objects.all()
    serializer = DetailSerializer
