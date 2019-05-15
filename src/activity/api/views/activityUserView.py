from activity.models import Activity
from ..serializers import ActivitySerializer
from rest_framework import viewsets

class ActivityUserViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    def get_queryset(self):
        username = self.kwargs['username']
        return Activity.objects.filter(user__username=username)
