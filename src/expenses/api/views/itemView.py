from expenses.models import Item
from ..serializers import ItemSerializers
from rest_framework import viewsets

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializers
    def get_queryset(self):
        reference = self.kwargs['reference']
        return Item.objects.filter(expense__reference=reference)
