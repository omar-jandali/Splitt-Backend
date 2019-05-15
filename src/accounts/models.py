from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    bank = models.CharField(max_length=52)
    type = models.SmallIntegerField(default=1) #1 = checking 2 = savings 3 = credit
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    primary = models.BooleanField(default=True)
    acct_ids = models.CharField(max_length=32)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + self.name

class Transaction(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE)
    user_to = models.CharField(max_length=32)
    acct_from = models.ForeignKey(Account, on_delete=models.CASCADE)
    acct_to = models.CharField(max_length=32)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=225)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_from.username + self.user_to
