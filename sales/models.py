from django.db import models
class Sale(models.Model):
    #product_name: tên sản phẩm (kiểu chuối kí tự)
    product_name = models.CharField(max_length=100)
    #weight: trọng lượng (kiểu số thực)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    #gold_price: giá vàng (kiểu số thực)
    gold_price = models.DecimalField(max_digits=10, decimal_places=2)
    #labor_cost: chi phí gia công
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2)
    #stone_cost:chi phí đá (Kiểu số thực.)
    stone_cost = models.DecimalField(max_digits=10, decimal_places=2)
    #sale_price: giá bán (Kiểu số thực)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    #created_at :ngày tạo (Kiểu ngày giờ.)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
# Create your models here.
