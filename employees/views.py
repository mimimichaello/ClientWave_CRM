from django.shortcuts import render
from django.urls import reverse_lazy

from employees.utils import filter_tasks, filter_customers, filter_orders, paginate_data

from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView

from django.contrib.auth import logout

from django.shortcuts import render, redirect

from employees.forms import EmployeeRegisterForm, EmployeeLoginForm

from employees.models import Employee
from customers.models import Customer
from orders.models import Order
from tasks.models import Task


class RegisterEmployeeView(CreateView):
    form_class = EmployeeRegisterForm
    template_name = 'employees/register_employee.html'
    extra_context = {
        'title': 'Регистрация'
    }

    success_url = reverse_lazy('login_employee')


class LoginEmployeeView(LoginView):
    form_class = EmployeeLoginForm
    template_name = 'employees/login_employee.html'
    extra_context = {
        'title': 'Авторизация'
    }

    def get_success_url(self):
        return reverse_lazy('home')


def logout_view(request):
    logout(request)
    return redirect('login_employee')


def home_view(request):
    return render(request, 'employees/home.html', {'title': 'Главная страница'})


def personal_account(request):
    employee = request.user
    customers = Customer.objects.all()
    orders = Order.objects.all()

    tasks = Task.objects.filter(assigned_to=employee)

    status_filter_tasks = request.GET.get('status_task')
    tasks = filter_tasks(tasks, status_filter_tasks)


    query = request.GET.get('query')
    status_filter = request.GET.get('status')
    payment_status_filter = request.GET.get('payment_status')

    customers = filter_customers(customers, query)
    orders = filter_orders(orders, status_filter, payment_status_filter)

    page_number = request.GET.get("page")
    page_obj = paginate_data(customers, page_number)

    page_number_orders = request.GET.get("page_orders")
    page_obj_orders = paginate_data(orders, page_number_orders)

    page_number_tasks = request.GET.get("page_tasks")
    page_obj_tasks = paginate_data(tasks, page_number_tasks)

    context = {
        'employee': employee,
        'customers': customers,
        'orders': orders,
        'tasks': tasks,
        'page_obj': page_obj,
        'page_obj_orders': page_obj_orders,
        'page_obj_tasks': page_obj_tasks,
        'title': 'Личный кабинет'
    }

    template = {
        'Sales Manager': 'employees/personal_account_sm.html',
        'Technical Support': 'employees/personal_account_ts.html',
        'Admin': 'employees/personal_account_admin.html'
    }

    template_name = template.get(employee.employee_category, 'employees/personal_account_default.html')
    return render(request, template_name, context)
