from accounts.models import Account
from ..serializers import AccountSerializer
from rest_framework import viewsets

class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    def get_queryset(self):
        username = self.kwargs['username']
        return Account.objects.filter(user__username = username)
