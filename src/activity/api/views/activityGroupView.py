from activity.models import Activity
from ..serializers import ActivitySerializer
from rest_framework import viewsets

class ActivityGroupViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    def get_queryset(self):
        reference = self.kwargs['reference']
        return Activity.objects.filter(group__reference=reference)
