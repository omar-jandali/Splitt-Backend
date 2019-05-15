from expenses.models import Expense
from ..serializers import ExpenseSerializers
from rest_framework import viewsets

class ExpensesViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializers
