from groups.models import Group

from rest_framework import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework import DestroyAPIView, RetrieveAPIView

from groups.api.serializers import GroupSerializer

class GroupCreateView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupListView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupRetrieveView(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupUpdateView(UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDestroyView(DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
