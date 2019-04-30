from Items.model import Item

from Item.api.serializers import ItemSerializers

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView,
from rest_framework.generics import UpdateAPIView, DestroyAPIView

class ItemCreateView(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemsSerializers

class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemsSerializers

class ItemRetrieveView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemsSerializers

class ItemUpdateView(UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemsSerializers

class ItemDeleteView(DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemsSerializers
