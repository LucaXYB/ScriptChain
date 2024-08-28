# question1/management/commands/populate_test_data.py

from django.core.management.base import BaseCommand
from question1.models import User, Order

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create 1000 users
        for i in range(1000):
            user = User.objects.create(username=f'User{i}', email=f'user{i}@example.com')
            # Create 10 orders for each user
            for j in range(10):
                Order.objects.create(order_number=f'Order{user.id}_{j}', user=user)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
