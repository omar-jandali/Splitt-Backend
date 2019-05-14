from groups.api.views.groupViews import GroupViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', GroupViewSet, base_name='groups')
urlpatterns = router.urls

# from django.urls import path
#
# from groups.api.views.groupViews import GroupCreateView, GroupListView, GroupRetrieveView
# from groups.api.views.groupViews import GroupDestroyView, GroupUpdateView
#
# urlpatterns = [
#     path('', GroupListView.as_view()),
#     path('create/', GroupCreateView.as_view()),
#     path('update/<pk>/', GroupUpdateView.as_view()),
#     path('destroy/<pk>/', GroupDestroyView.as_view()),
#     path('<pk>/', GroupRetrieveView.as_view())
# ]

# api/group/
# api/group/create
# api/group/update/pk
# api/group/delete/pk
# api/group/pk
