from groups.api.views.memberViews import MemberViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'(?P<reference>[-\w]+)', MemberViewSet, base_name='member')
urlpatterns = router.urls

# from django.urls import path
#
# from groups.api.views.memberViews import MemberCreateView, MemberListView, MemberRetrieveView
# from groups.api.views.memberViews import MemberDestroyView, MemberUpdateView
#
# urlpatterns = [
#     path('', MemberListView.as_view()),
#     path('create/', MemberCreateView.as_view()),
#     path('update/<pk>/', MemberUpdateView.as_view()),
#     path('destroy/<pk>/', MemberDestroyView.as_view()),
#     path('<pk>/', MemberRetrieveView.as_view())
# ]
#
# # api/group/member/
# api/group/member/create
# api/group/member/update/pk
# api/group/member/delete/pk
# api/group/member/pk
