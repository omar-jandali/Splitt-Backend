from expenses.models import Item

from expenses.api.serializers import ItemSerializers

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.generics import UpdateAPIView, DestroyAPIView

class ItemCreateView(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers

class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers

class ItemRetrieveView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers

class ItemUpdateView(UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers

class ItemDeleteView(DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers
