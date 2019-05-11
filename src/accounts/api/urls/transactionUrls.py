from django.urls import path

from accounts.api.views.transactionView import TransactionCreateView, TransactionListView, TransactionRetrieveView
from accounts.api.views.transactionView import TransactionDestroyView, TransactionUpdateView

urlpatterns = [
    path('', TransactionListView.as_view()),
    path('create/', TransactionCreateView.as_view()),
    path('update/<pk>/', TransactionUpdateView.as_view()),
    path('delete/<pk>/', TransactionDestroyView.as_view()),
    path('<pk>/', TransactionRetrieveView.as_view())
]

# api/account/transaction/
# api/account/transaction/create
# api/account/transaction/update/pk
# api/account/transaction/delete/pk
# api/account/transaction/pk
