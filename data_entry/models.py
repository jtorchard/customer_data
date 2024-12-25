# Create your models here.
import datetime

from django.db import models
from django.utils import timezone


class Customer(models.Model):
    given_names = models.CharField(max_length=100)
    surname = models.CharField(max_length=60)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.surname

    def was_added_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Licence(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    given_names = models.CharField(max_length=100)
    surname = models.CharField(max_length=60)
    pub_date = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateTimeField()
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    number = models.CharField(max_length=60)
    address = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.number}"


class BankAccount(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    account_number = models.CharField(max_length=12)
    notes = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.account_number
