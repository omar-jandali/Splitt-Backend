from groups.api.views.groupMembersView import GroupMemberViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'(?P<reference>[-\w]+)', GroupMemberViewSet, base_name='group_members')
urlpatterns = router.urls
