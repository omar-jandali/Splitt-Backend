from accounts.api.views.transactionView import TransactionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'(?P<acct_ids>[-\w]+)', TransactionViewSet, base_name='transaction')
urlpatterns = router.urls
