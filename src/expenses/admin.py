from django.contrib import admin

from .models import Expense, Item

admin.site.register(Expense)
admin.site.register(Item)
