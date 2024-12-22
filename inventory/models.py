from django.db import models

class Inventory(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
