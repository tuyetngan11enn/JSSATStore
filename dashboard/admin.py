from django.contrib import admin
from .models import Dashboard  # Đảm bảo mô hình 'Dashboard' có tồn tại trong models.py

admin.site.register(Dashboard)