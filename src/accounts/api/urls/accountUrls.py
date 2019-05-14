from accounts.api.views.accountView import AccountViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', AccountViewSet, base_name='account')
urlpatterns = router.urls

# from django.urls import path
#
# from accounts.api.views.accountView import AccountCreateView, AccountListView, AccountRetrieveView
# from accounts.api.views.accountView import AccountDestroyView, AccountUpdateView
#
# urlpatterns = [
#     path('', AccountListView.as_view()),
#     path('create/', AccountCreateView.as_view()),
#     path('update/<pk>/', AccountUpdateView.as_view()),
#     path('delete/<pk>/', AccountDestroyView.as_view()),
#     path('<pk>/', AccountRetrieveView.as_view())
# ]

# api/account/
# api/account/create
# api/account/update/pk
# api/account/delete/pk
# api/account/pk
