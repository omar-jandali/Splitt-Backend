from django.urls import path

from activity.api.views.activityView import ActivityCreateView, ActivityListView, ActivityRetrieveView
from activity.api.views.activityView import ActivityDeleteView, ActivityUpdateView

urlpatterns = [
    path('', ActivityListView.as_view()),
    path('create/', ActivityCreateView.as_view()),
    path('update/<pk>/', ActivityUpdateView.as_view()),
    path('delete/<pk>/', ActivityDeleteView.as_view()),
    path('<pk>/', ActivityRetrieveView.as_view())
]
