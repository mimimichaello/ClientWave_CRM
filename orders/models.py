from django.db import models

from customers.models import Customer

class Order(models.Model):

    STATUS_CHOICES = [
        ('В обработке', 'В обработке'),
        ('Выполнен', 'Выполнен'),
        ('Отменен', 'Отменен'),
        ('Ожидает отправки', 'Ожидает отправки'),
        ('Отправлен', 'Отправлен'),
    ]

    PAYMENT_CHOICES = [
        ('Оплачен', 'Оплачен'),
        ('Не оплачен', 'Не оплачен'),
    ]


    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='В обработке', choices=STATUS_CHOICES)
    shipping_address = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=11, choices=PAYMENT_CHOICES, default='Не оплачен')
    transaction_id = models.CharField(max_length=100)


    def __str__(self):
        return f'Order {self.id} - {self.customer}'
