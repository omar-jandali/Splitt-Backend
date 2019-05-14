"""splitt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/user/profile/', include('users.api.urls.profileUrls')),
    path('api/user/detail/', include('users.api.urls.detailUrls')),
    path('api/user/friend/', include('users.api.urls.friendUrls')),
    path('api/users/', include('users.api.urls.userUrls')),

    path('api/members/', include('groups.api.urls.memberUrls')),
    path('api/group/members/', include('groups.api.urls.groupMemberUrls')),
    path('api/groups/', include('groups.api.urls.groupsUrls')),
    path('api/group/', include('groups.api.urls.groupUrls')),

    path('api/expense/items/', include('expenses.api.urls.expenseUrls')),
    path('api/expenses/', include('expenses.api.urls.itemUrls')),

    path('api/account/transaction/', include('accounts.api.urls.transactionUrls')),
    path('api/accounts/', include('accounts.api.urls.accountUrls')),

    path('api/activity/', include('activity.api.urls.activityUrls'))
]
