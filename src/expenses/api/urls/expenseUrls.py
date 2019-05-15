from expenses.api.views.expenseView import ExpenseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'(?P<reference>[-\w]+)', ExpenseViewSet, base_name='expense')
urlpatterns = router.urls
