from django.urls import path

from accounts.api.views.transactionViews import TransactionCreateView, TransactionListView, TransactionRetrieveView
from accounts.api.views.transactionViews import TransactionDestroyView, TransactionUpdateView

urlpatterns = [
    path('', TransactionListView.as_view()),
    path('create/', TransactionCreateView.as_view()),
    path('update/<pk>/', TransactionUpdateView.as_view()),
    path('delete/<pk>/', TransactionDeleteView.as_view()),
    path('<pk>/', TransactionRetrieveView.as_view())
]

# api/account/transaction/
# api/account/transaction/create
# api/account/transaction/update/pk
# api/account/transaction/delete/pk
# api/account/transaction/pk
