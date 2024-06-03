from django.urls import path

from employees.views import RegisterEmployeeView, LoginEmployeeView, logout_view, home_view, personal_account

urlpatterns = [
    path('register_employee/', RegisterEmployeeView.as_view(), name='register_employee'),
    path('login_employee/', LoginEmployeeView.as_view(), name='login_employee'),
    path('logout_employee/', logout_view, name='logout_employee'),
    path('home', home_view, name='home'),
    path('personal_account', personal_account, name='personal_account'),
]
