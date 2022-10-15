from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime
# from user_app.models.account_model import Profile
from .category_model import Category
from django import forms


# @python_2_unicode_compatible
class Product(models.Model):
    p_title = models.CharField(max_length=255, null=True, default=None)
    p_name = models.CharField(max_length=100, null=True, default=None)
    p_code = models.CharField(max_length=50)
    p_image = models.ImageField(upload_to='products/', null=True, default=None)
    p_description = models.TextField(max_length=1000, null=True, default=None)
    p_country = models.CharField(max_length=50, null=True, default=None)
    created_at = models.DateTimeField(null=True, default=datetime.now, blank=True)
    updated_at = models.DateTimeField(null=True, default=datetime.now, blank=True)  # auto_now_add=True
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # category = models.ManyToManyField(Category, help_text='Select a Category for this Product')
    middles = models.ManyToManyField(Category, through='Middleship')

    def __str__(self):
        return self.p_title
        # return f"{self.p_title}, {self.p_name}, {self.p_code}, {self.p_date}, {self.p_country}"

    # def __unicode__(self):
    #     return u"%s" % self.user

    class Meta:
        ordering = ['created_at', 'p_name']
        managed = True
        db_table = 'catalog_product'
        verbose_name = 'catalog_product'
        verbose_name_plural = 'catalog_products'


class Middleship(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_joined = models.DateField(null=True, default=datetime.now)

    def __str__(self):
        return "{}_{}".format(self.Product.__str__(), self.Category.__str__())
