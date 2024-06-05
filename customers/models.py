from django.db import models


class Customer(models.Model):

    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
    ]


    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    notes = models.TextField(blank=True, null=True)



    def __str__(self):
        return f'{self.first_name} {self.last_name}'
