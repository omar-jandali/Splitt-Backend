from django.urls import path

from users.api.views.detailViews import DetailListView, DetailRetrieveView, DetailCreateView
from users.api.views.detailViews import DetailDestroyView, DetailUpdateView

urlpatterns = [
    path('', DetailListView.as_view()),
    path('create/', DetailCreateView.as_view()),
    path('update/<pk>/', DetailUpdateView.as_view()),
    path('delete/<pk>/', DetailDestroyView.as_view()),
    path('<pk>/', DetailRetrieveView.as_view())
]

# api/users/detail/ - done
# api/users/detail/create - done
# api/users/detail/update/pk - done
# api/users/detail/delete/pk - done
# api/users/detail/pk - done
