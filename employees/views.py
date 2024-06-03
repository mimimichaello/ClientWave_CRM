from django.shortcuts import render
from django.urls import reverse_lazy

from django.core.paginator import Paginator

from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView

from django.contrib.auth import logout

from django.shortcuts import render, redirect

from employees.forms import EmployeeRegisterForm, EmployeeLoginForm

from employees.models import Employee


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
    context = {
        'employee': employee,
        'title': 'Личный кабинет'
    }
    if employee.employee_category == 'Sales Manager':
        return render(request, 'employees/personal_account_sm.html', context)
    elif employee.employee_category == 'Technical Support':
        return render(request, 'employees/personal_account_ts.html', context)
    elif employee.employee_category == 'Admin':
        return render(request, 'employees/personal_account_admin.html', context)
