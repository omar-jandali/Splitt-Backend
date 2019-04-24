from django.urls import path

from ..views.userViews import UserListView, UserRetrieveView, UserCreateView
from ..views.userViews import UserDestroyView, UserUpdateView

urlpatterns = [
    path('', UserListView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('update/<pk>/', UserUpdateView.as_view()),
    path('delete/<pk>/', UserDestroyView.as_view()),
    path('<pk>/', UserRetrieveView.as_view())
]
