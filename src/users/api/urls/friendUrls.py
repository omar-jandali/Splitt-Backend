from django.urls import path

from users.api.views.friendViews import FriendListView, FriendRetrieveView, FriendCreateView
from users.api.views.friendViews import FriendDestroyView, FriendUpdateView

urlpatterns = [
    path('', FriendListView.as_view()),
    path('create/', FriendCreateView.as_view()),
    path('update/<pk>/', FriendUpdateView.as_view()),
    path('delete/<pk>/', FriendDestroyView.as_view()),
    path('<pk>/', FriendRetrieveView.as_view())
]

# api/users/friend/ - done
# api/users/friend/create - done
# api/users/friend/update/pk - done
# api/users/friend/delete/pk - done
# api/users/friend/pk - done
