from accounts.models import Transaction

from accounts.api.serializers import TransactionSerializer

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView

class TransactionCreateView(CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionListView(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionRetrieveView(RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionUpdateView(UpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDestroyView(DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
