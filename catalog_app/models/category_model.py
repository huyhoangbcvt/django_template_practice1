from django.db import models
from django.contrib.auth.models import User
# from .product_model import Product
from datetime import datetime


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='catalogs/', null=True, default=None)
    content = models.TextField(max_length=1000, null=True, default=None)
    created_at = models.DateTimeField(null=True, default=datetime.now, blank=True)
    updated_at = models.DateTimeField(null=True, default=datetime.now, blank=True) # auto_now_add=True
    user = models.ForeignKey(User, on_delete=models.CASCADE) # One- Many
    # product = models.ManyToManyField(Product, help_text='Select a Product for this Catalog')
    PRODUCT_CHOICES = ()
    product_map = models.PositiveSmallIntegerField(choices=PRODUCT_CHOICES, null=True, default=0, blank=True)

    # Ko có cái này thì table tạo ra theo appname_classmodel
    # class Meta:
    #     managed = True
    #     db_table = 'catalogapp_catalog'
    class Meta:
        ordering = ['created_at', 'title']
        managed = True
        db_table = 'catalog_category'
        verbose_name = 'catalog_category'
        verbose_name_plural = 'catalog_categories'

    def __str__(self):
        return self.title
        # return f"{self.title}, {self.image}, {self.body}, {self.user}"
