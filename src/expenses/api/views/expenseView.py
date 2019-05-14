from expenses.models import Expense
from ..serializers import ExpensesSerializers
from rest_framework import viewsets

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpensesSerializers

# from expenses.models import Expense
#
# from expenses.api.serializers import ExpensesSerializers
#
# from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
# from rest_framework.generics import UpdateAPIView, DestroyAPIView
#
# class ExpenseCreateView(CreateAPIView):
#     queryset = Expense.objects.all()
#     serializer_class = ExpensesSerializers
#
# class ExpenseListView(ListAPIView):
#     queryset = Expense.objects.all()
#     serializer_class = ExpensesSerializers
#
# class ExpenseRetrieveView(RetrieveAPIView):
#     queryset = Expense.objects.all()
#     serializer_class = ExpensesSerializers
#
# class ExpenseUpdateView(UpdateAPIView):
#     queryset = Expense.objects.all()
#     serializer_class = ExpensesSerializers
#
# class ExpenseDeleteView(DestroyAPIView):
#     queryset = Expense.objects.all()
#     serializer_class = ExpensesSerializers
