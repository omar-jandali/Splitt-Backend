from accounts.models import Transaction
from ..serializers import TransactionSerializer
from rest_framework import viewsets

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    def get_queryset(self):
        account_id = self.kwargs['acct_ids']
        return Transaction.objects.filter(acct_from__acct_ids = account_id)
