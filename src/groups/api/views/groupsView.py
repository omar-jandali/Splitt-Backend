from groups.models import Group
from ..serializers import GroupSerializer
from rest_framework import viewsets

class GroupsViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
