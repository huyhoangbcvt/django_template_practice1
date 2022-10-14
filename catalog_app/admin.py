from django.contrib import admin
from .models.product_model import Product
from .models.category_model import Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)