from groups.api.views.groupView import GroupViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'(?P<reference>[-\w]+)', GroupViewSet, base_name='group')
urlpatterns = router.urls
