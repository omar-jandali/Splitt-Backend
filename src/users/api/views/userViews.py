from django.contrib.auth.models import User
from ..serializers import UserSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#
# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
# from rest_framework.generics import DestroyAPIView, UpdateAPIView
#
#
#
# class UserListView(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserRetrieveView(RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserCreateView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDestroyView(DestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserUpdateView(UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
