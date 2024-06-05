from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect

from tasks.models import Task

def filter_customers(customers, query):
    if query:
        return customers.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query) |
            Q(address__icontains=query)
        )
    return customers

def filter_orders(orders, status_filter, payment_status_filter):
    if status_filter:
        orders = orders.filter(status=status_filter)

    if payment_status_filter:
        orders = orders.filter(payment_status=payment_status_filter)

    return orders

def paginate_data(data, page_number, items_per_page=5):
    paginator = Paginator(data, items_per_page)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return page_obj


def filter_tasks(tasks, status_filter_tasks):
    if status_filter_tasks:
        tasks = tasks.filter(status_task=status_filter_tasks)
    return tasks
