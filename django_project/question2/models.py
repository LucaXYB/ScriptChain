# question2/models.py

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.username

class Order(models.Model):
    order_number = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.order_number


