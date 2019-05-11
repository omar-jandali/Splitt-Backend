from expenses.api.views.ItemView import ItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ItemViewSet, base_name='item')
urlpatterns = router.urls

# from django.urls import path
#
# from expenses.api.views.itemView import ItemCreateView, ItemListView, ItemRetrieveView
# from expenses.api.views.itemView import ItemDeleteView, ItemUpdateView
#
# urlpatterns = [
#     path('', ItemListView.as_view()),
#     path('create/', ItemCreateView.as_view()),
#     path('update/<pk>/', ItemUpdateView.as_view()),
#     path('delete/<pk>/', ItemDeleteView.as_view()),
#     path('<pk>/', ItemRetrieveView.as_view())
# ]

# api/group/member/
# api/group/member/create
# api/group/member/update/pk
# api/group/member/delete/pk
# api/group/member/pk
