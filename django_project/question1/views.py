from django.shortcuts import render
from .models import Order, User
from django.db import connection
import time
import psutil

# Helper function to get memory usage
def get_memory_usage():
    process = psutil.Process()
    mem_info = process.memory_info()
    return mem_info.rss / (1024 ** 2)  # Convert to MB

#### Create your views here.

### Using select_related to fetch orders and their associated user information.
## Advantages:
# - Fewer queries, typically only one query.
# - Very efficient for one-to-one and many-to-one relationships.
## Disadvantages:
# - Not ideal for many-to-many or one-to-many relationships as it may lead to redundant data loading.
# - Complex SQL JOINs can increase database load.
def orders_with_users(request):
    # Clear the query log
    connection.queries_log.clear()
    # Record the start time
    start_time = time.time()

    # Record initial memory usage
    initial_memory = get_memory_usage()

    # Using select_related to fetch orders and their associated users 
    orders = list(Order.objects.select_related('user').all())  # Load data into memory
    for order in orders:
        _ = order.user.username  

    # Calculate the number of queries and the elapsed time
    query_count = len(connection.queries)
    elapsed_time = time.time() - start_time

    # Record final memory usage
    final_memory = get_memory_usage()
    memory_usage = final_memory - initial_memory

    # Estimate database load (for demonstration purposes)
    database_load = query_count * 10  # Arbitrary load factor

    return render(request, 'question1/order_list.html', {
        'orders': orders,
        'query_count': query_count,
        'elapsed_time': elapsed_time,
        'memory_usage': memory_usage,
        'database_load': database_load,
    })


### Use prefetch_related to retrieve users and all their related order information.
## Advantages:
# - Suitable for one-to-many or many-to-many relationships, avoids complex JOINs.
# - Lower memory usage as it avoids redundant data loading.
## Disadvantages:
# - More queries are executed since each related model requires a separate query.
# - In some cases, the overall query time may increase due to multiple queries.
def users_with_orders(request):
    # Clear the query log
    connection.queries_log.clear()
    # Record the start time
    start_time = time.time()

    # Record initial memory usage
    initial_memory = get_memory_usage()

    # Using prefetch_related to fetch users and their associated orders
    users = list(User.objects.prefetch_related('order_set').all())  # Load data into memory
    for user in users:
        _ = list(user.order_set.all())  

    # Calculate the number of queries and the elapsed time
    query_count = len(connection.queries)
    elapsed_time = time.time() - start_time

    # Record final memory usage
    final_memory = get_memory_usage()
    memory_usage = final_memory - initial_memory

    # Estimate database load (for demonstration purposes)
    database_load = query_count * 10  # Arbitrary load factor

    return render(request, 'question1/user_list.html', {
        'users': users,
        'query_count': query_count,
        'elapsed_time': elapsed_time,
        'memory_usage': memory_usage,
        'database_load': database_load,
    })


# View to display a comparison between select_related and prefetch_related
def compare_related_methods(request):
    # Clear previous query logs
    connection.queries_log.clear()

    # Measure select_related performance
    start_time = time.time()
    initial_memory = get_memory_usage()

    orders = list(Order.objects.select_related('user').all())
    for order in orders:
        _ = order.user.username  # Ensure related data is loaded

    select_query_count = len(connection.queries)
    select_elapsed_time = time.time() - start_time
    select_memory_usage = get_memory_usage() - initial_memory
    select_database_load = select_query_count * 10  # Arbitrary load factor

    # Clear query log for the next test
    connection.queries_log.clear()

    # Measure prefetch_related performance
    start_time = time.time()
    initial_memory = get_memory_usage()

    users = list(User.objects.prefetch_related('order_set').all())
    for user in users:
        _ = list(user.order_set.all())  # Ensure related data is loaded

    prefetch_query_count = len(connection.queries)
    prefetch_elapsed_time = time.time() - start_time
    prefetch_memory_usage = get_memory_usage() - initial_memory
    prefetch_database_load = prefetch_query_count * 10  # Arbitrary load factor

    return render(request, 'question1/compare_methods.html', {
        'select_query_count': select_query_count,
        'select_elapsed_time': select_elapsed_time,
        'select_memory_usage': select_memory_usage,
        'select_database_load': select_database_load,
        'prefetch_query_count': prefetch_query_count,
        'prefetch_elapsed_time': prefetch_elapsed_time,
        'prefetch_memory_usage': prefetch_memory_usage,
        'prefetch_database_load': prefetch_database_load,
    })