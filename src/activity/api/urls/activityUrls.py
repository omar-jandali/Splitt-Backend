from activity.api.views.activityView import ActivityViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ActivityViewSet, base_name='activity')
urlpatterns = router.urls

# from django.urls import
#
# from activity.api.views.activityView import ActivityCreateView, ActivityListView, ActivityRetrieveView
# from activity.api.views.activityView import ActivityDeleteView, ActivityUpdateView
#
# urlpatterns = [
#     path('', ActivityListView.as_view()),
#     path('create/', ActivityCreateView.as_view()),
#     path('update/<pk>/', ActivityUpdateView.as_view()),
#     path('delete/<pk>/', ActivityDeleteView.as_view()),
#     path('<pk>/', ActivityRetrieveView.as_view())
# ]
