from accounts.api.views.accountsView import AccountsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', AccountsViewSet, base_name='account')
urlpatterns = router.urls
