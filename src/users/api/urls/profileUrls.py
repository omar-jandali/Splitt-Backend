from django.urls import path

from users.api.views.profileViews import ProfileListView, ProfileRetrieveView, ProfileCreateView
from users.api.views.profileViews import ProfileDestroyView, ProfileUpdateView

urlpatterns = [
    path('', ProfileListView.as_view()),
    path('create/', ProfileCreateView.as_view()),
    path('update/<pk>/', ProfileUpdateView.as_view()),
    path('delete/<pk>/', ProfileDestroyView.as_view()),
    path('<pk>/', ProfileRetrieveView.as_view())
]

# api/users/profile/ - done
# api/users/profile/create
# api/users/profile/update/pk
# api/users/profile/delete/pk
# api/users/profile/pk
