from expenses.models import Account
from ..serializers import AccountSerializer
from rest_framework import viewsets

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

# from accounts.models import Account
#
# from accounts.api.serializers import AccountSerializer
#
# from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
# from rest_framework.generics import DestroyAPIView, UpdateAPIView
#
# class AccountCreateView(CreateAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer
#
# class AccountListView(ListAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer
#
# class AccountRetrieveView(RetrieveAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer
#
# class AccountUpdateView(UpdateAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer
#
# class AccountDestroyView(DestroyAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer
