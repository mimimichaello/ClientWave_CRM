from django.utils import timezone
from django.db import models

from employees.models import Employee

class Task(models.Model):

    STATUS_CHOICES = [
        ('Выполнено', 'Выполнено'),
        ('В работе', 'В работе'),
        ('Просрочено', 'Просрочено'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateField()
    status_task = models.CharField(max_length=12, choices=STATUS_CHOICES)
    assigned_to = models.ForeignKey(Employee, related_name='tasks_assigned_to', on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(Employee, related_name='tasks_assigned_by', on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if self.deadline < timezone.now().date() and self.status != 'Выполнено':
            self.status = 'Просрочено'
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.name} - {self.get_status_display()} - Исполнитель: {self.assigned_to}"
