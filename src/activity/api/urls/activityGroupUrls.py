from activity.api.views.activityGroupView import ActivityGroupViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'(?P<reference>[-\w]+)', ActivityGroupViewSet, base_name='activity')
urlpatterns = router.urls
