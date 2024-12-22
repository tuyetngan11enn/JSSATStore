from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# Create your models here.
