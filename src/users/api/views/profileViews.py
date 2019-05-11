from users.models import Profile
from ..serializers import ProfileSerializer
from rest_framework import viewsets

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# from users.models import Profile
#
# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
# from rest_framework.generics import DestroyAPIView, UpdateAPIView
#
# from users.api.serializers import ProfileSerializer
#
#
# class ProfileListView(ListAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#
#
# class ProfileRetrieveView(RetrieveAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#
#
# class ProfileCreateView(CreateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#
#
# class ProfileDestroyView(DestroyAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#
#
# class ProfileUpdateView(UpdateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
