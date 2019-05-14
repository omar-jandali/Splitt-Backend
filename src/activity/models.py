from django.db import models
from django.contrib.auth.models import User

from accounts.models import Account, Transaction
from expenses.models import Expense, Item
from groups.models import Group, Member
from users.models import Profile, Detail

class Activity(models.Model):
    type = models.SmallIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=225)
    verified = models.BooleanField(default=False)
    seen = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type + self.description
