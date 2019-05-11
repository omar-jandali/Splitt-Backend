from users.api.views.userViews import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UserViewSet, base_name='user')
urlpatterns = router.urls


# from django.urls import path
#
# from ..views.userViews import UserListView, UserRetrieveView, UserCreateView
# from ..views.userViews import UserDestroyView, UserUpdateView
#
# urlpatterns = [
#     path('', UserListView.as_view()),
#     path('create/', UserCreateView.as_view()),
#     path('update/<pk>/', UserUpdateView.as_view()),
#     path('delete/<pk>/', UserDestroyView.as_view()),
#     path('<pk>/', UserRetrieveView.as_view())
# ]

# api/users/ - done
# api/users/create - done
# api/users/update/pk - done
# api/users/delete/pk - done
# api/users/pk - done
