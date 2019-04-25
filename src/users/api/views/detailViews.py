from users.models import Detail

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView

from users.api.serializers import DetailSerializer


class DetailListView(ListAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer


class DetailRetrieveView(RetrieveAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer


class DetailCreateView(CreateAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer


class DetailDestroyView(DestroyAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer


class DetailUpdateView(UpdateAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
