from activity.models import Activity

from activity.api.serializers import ActivitySerializers

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.generics import UpdateAPIView, DestroyAPIView

class ActivityCreateView(CreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializers

class ActivityListView(ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializers

class ActivityRetrieveView(RetrieveAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializers

class ActivityUpdateView(UpdateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializers

class ActivityDeleteView(DestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializers
