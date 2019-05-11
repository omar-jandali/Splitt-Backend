from groups.models import Group
from ..serializers import GroupSerializer
from rest_framework import viewsets

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# from groups.models import Group
#
# from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
# from rest_framework.generics import DestroyAPIView, UpdateAPIView
#
# from groups.api.serializers import GroupSerializer
#
# class GroupCreateView(CreateAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#
# class GroupListView(ListAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#
# class GroupRetrieveView(RetrieveAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#
# class GroupUpdateView(UpdateAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#
# class GroupDestroyView(DestroyAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
