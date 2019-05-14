from django.contrib.auth.models import User
from ..serializers import UserSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    lookup_field = 'username'
    queryset = User.objects.all()

    # def get_queryset(self):
    #     queryset = User.objects.all()
    #     username = self.request.query_params.get('username', None)
    #     if username is not None:
    #         queryset = queryset.filter(username = username)
    #     return queryset

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
