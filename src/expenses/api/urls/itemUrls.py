from expenses.api.views.itemView import ItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'(?P<reference>[-\w]+)', ItemViewSet, base_name='item')
urlpatterns = router.urls
