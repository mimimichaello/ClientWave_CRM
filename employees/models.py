from django.db import models

from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    EMPLOYEE_CHOICES = [
        ('Sales Manager', 'Sales Manager'),
        ('Technical Support', 'Technical Support'),
        ('Admin', 'Admin'),
    ]

    employee_category = models.CharField(max_length=20, choices=EMPLOYEE_CHOICES, default='Sales Manager')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

