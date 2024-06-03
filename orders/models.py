from django.db import models

from customers.models import Customer

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class OrderProduct(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


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
    products = models.ManyToManyField('Product', through='OrderProduct')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='В обработке')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='Не оплачен')
    delivery_date = models.DateField(null=True, blank=True)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        total_price = sum(
            order_product.product.price * order_product.quantity
            for order_product in self.orderproduct_set.all()
        )
        self.total_price = total_price
        super(Order, self).save(*args, **kwargs)


    def __str__(self):
        return f'Заказ №{self.id} - Статус: {self.status}, Общая стоимость: {self.total_price}'
