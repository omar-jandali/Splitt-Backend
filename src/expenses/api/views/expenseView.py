from expenses.models import Expense
from ..serializers import ExpenseSerializers
from rest_framework import viewsets

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializers
    def get_queryset(self):
        reference = self.kwargs['reference']
        return Expense.objects.filter(group__reference=reference)
