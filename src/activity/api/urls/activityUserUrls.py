from activity.api.views.activityUserView import ActivityUserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'(?P<username>[-\w]+)', ActivityUserViewSet, base_name='activity')
urlpatterns = router.urls
