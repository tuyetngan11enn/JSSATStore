from django.db import models

class Warranty(models.Model):
    product_name = models.CharField(max_length=100)
    warranty_period = models.IntegerField()  # Số tháng bảo hành
    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} - {self.warranty_period} months"

# Create your models here.
