from accounts.api.views.accountView import AccountViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'(?P<username>[-\w]+)', AccountViewSet, base_name='account')
urlpatterns = router.urls
