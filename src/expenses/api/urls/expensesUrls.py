from expenses.api.views.expensesView import ExpensesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ExpensesViewSet, base_name='expense')
urlpatterns = router.urls
