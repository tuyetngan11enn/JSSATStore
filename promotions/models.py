from django.db import models

class Promotions(models.Model):
    name = models.CharField(max_length=100)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

# Create your models here.
