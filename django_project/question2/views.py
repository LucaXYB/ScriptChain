from django.shortcuts import render
from .models import Order, User
from django.db.models import Q

def q_object_queries(request):
    # OR Query: Find orders with users whose username contains "John" or email ends with "example.com"
    orders_or_query = Order.objects.filter(
        Q(user__username__contains='John') | Q(user__email__endswith='example.com')
    )

    # AND Query: Find orders with users whose username contains "John" and total price greater than $500
    orders_and_query = Order.objects.filter(
        Q(user__username__contains='John') & Q(total_price__gt=500)
    )

    # NOT Query: Find orders with total price less than $100, excluding those with users whose username contains "John"
    orders_not_query = Order.objects.filter(
        Q(total_price__lt=100) & ~Q(user__username__contains='John')
    )

    # Combined Q objects: Find orders with users whose username contains "John" or "Jane" and email ends with "example.com"
    orders_combined_query = Order.objects.filter(
        (Q(user__username__contains='John') | Q(user__username__contains='Jane')) &
        Q(user__email__endswith='example.com')
    )

    # Nested Q objects: Find orders with total price greater than $500 or username does not contain "John" and email ends with "example.com"
    orders_nested_query = Order.objects.filter(
        Q(total_price__gt=500) | (Q(user__username__contains='John') & Q(user__email__endswith='example.com'))
    )

    context = {
        'orders_or_query': orders_or_query,
        'orders_and_query': orders_and_query,
        'orders_not_query': orders_not_query,
        'orders_combined_query': orders_combined_query,
        'orders_nested_query': orders_nested_query,
    }

    return render(request, 'question2/q_object_queries.html', context)
