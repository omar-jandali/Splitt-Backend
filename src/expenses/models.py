from django.db import models
from django.contrib.auth.models import User

from groups.models import Group

class Expense(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=42)
    split = models.SmallIntegerField(default=1)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    tax = models.DecimalField(max_digits=12, decimal_places=2)
    tip = models.DecimalField(max_digits=12, decimal_places=2)
    reference = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group.name + self.user.username

class Item(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    requested = models.CharField(max_length=32)
    description = models.CharField(max_length=225)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    paid = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    reference = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.expense.location + self.user.username
