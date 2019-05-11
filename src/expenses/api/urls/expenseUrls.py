from expenses.api.views.ExpenseView import ExpenseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ExpenseViewSet, base_name='expense')
urlpatterns = router.urls

# from django.urls import path
#
# from expenses.api.views.expenseView import ExpenseCreateView, ExpenseListView, ExpenseRetrieveView
# from expenses.api.views.expenseView import ExpenseDeleteView, ExpenseUpdateView
#
# urlpatterns = [
#     path('', ExpenseListView.as_view()),
#     path('create/', ExpenseCreateView.as_view()),
#     path('update/<pk>/', ExpenseUpdateView.as_view()),
#     path('delete/<pk>/', ExpenseDeleteView.as_view()),
#     path('<pk>/', ExpenseRetrieveView.as_view())
# ]

# api/group/member/
# api/group/member/create
# api/group/member/update/pk
# api/group/member/delete/pk
# api/group/member/pk
