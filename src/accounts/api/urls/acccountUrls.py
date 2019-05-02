from django.urls import path

from accounts.api.views.accountViews import AccountCreateView, AccountListView, AccountRetrieveView
from accounts.api.views.accountViews import AccountDestroyView, AccountUpdateView

urlpatterns = [
    path('', AccountListView.as_view()),
    path('create/', AccountCreateView.as_view()),
    path('update/<pk>/', AccountUpdateView.as_view()),
    path('delete/<pk>/', AccountDeleteView.as_view()),
    path('<pk>/', AccountRetrieveView.as_view())
]

# api/account/
# api/account/create
# api/account/update/pk
# api/account/delete/pk
# api/account/pk
