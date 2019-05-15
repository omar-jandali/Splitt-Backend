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

    path('api/expense/items/', include('expenses.api.urls.itemUrls')),
    path('api/expenses/', include('expenses.api.urls.expensesUrls')),
    path('api/expense/', include('expenses.api.urls.expenseUrls')),

    path('api/account/transaction/', include('accounts.api.urls.transactionUrls')),
    path('api/account/', include('accounts.api.urls.accountUrls')),
    path('api/accounts/', include('accounts.api.urls.accountsUrls')),

    path('api/activity/user/', include('activity.api.urls.activityUserUrls')),
    path('api/activity/group/', include('activity.api.urls.activityGroupUrls'))
]

# admin/ => this is a link to the django admin page (managemant)
# api/user/profile/(username) => returns all profiles or user profile
# api/user/detail/(username) => returns all details or user details
# api/user/friend/(username) => returns all friends or user sent friend request
    # might create two endpoints 1 -> friender 2 => friended
# api/users/(username) => returns all users or passed in users username

# api/members/<username> => list all of the member objects a user is included in
# api/group/members/<reference> => grabs all of the members in a group based on group reference
# api/groups/ => list all of the groups in the database
# api/groups/<reference> => list grabs a specific group based on the reference

# api/expense/items/<reference> => grabs all of the items related to an expense based on reference
# api/expenses/ => grabs all of the expenses in the database
# api/expense/<reference> => grabs an expense based on the reference that is passed

# api/account/transaction/<acct_ids> => this retreives all of the transactions related to an account
# api/account/<username> => grabs all of the accounts for a singel user based on username
# api/account/ =>  grabs all of the accounts in the database

# api/activity/user/<username> => Grabs all of the activity based on the users username
# api/activity/group/<reference> => grabs all of the activity for a group based on reference  
