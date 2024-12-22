from django.db import models


class SalesReport(models.Model):
    date = models.DateField()  # Ngày thống kê
    total_revenue = models.DecimalField(max_digits=12, decimal_places=2)  # Tổng doanh thu
    total_sales = models.IntegerField()  # Tổng số đơn hàng
    total_customers = models.IntegerField()  # Tổng số khách hàng

    def __str__(self):
        return f"Report for {self.date}"

# Create your models here.
