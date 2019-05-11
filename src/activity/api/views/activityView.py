from activity.models import Activity

from activity.api.serializers import ActivitySerializer

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.generics import UpdateAPIView, DestroyAPIView

class ActivityCreateView(CreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityListView(ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityRetrieveView(RetrieveAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityUpdateView(UpdateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityDeleteView(DestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
