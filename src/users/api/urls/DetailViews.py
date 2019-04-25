from django.urls import path

from users.api.views.profileViews import DetailListView, DetailRetrieveView, DetailCreateView
from users.api.views.profileViews import DetailDestroyView, DetailUpdateView

urlpatterns = [
    path('', DetailListView.as_view()),
    path('create/', DetailCreateView.as_view()),
    path('update/<pk>/', DetailUpdateView.as_view()),
    path('delete/<pk>/', DetailDestroyView.as_view()),
    path('<pk>/', DetailRetrieveView.as_view())
]
