from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime
from user_app.models.account_model import Author

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
    # user = models.OneToOneField(User, on_delete=models.CASCADE)  # id table user
    author  = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    # catalog = models.ManyToManyField(Category, help_text='Select a Catalog for this Product')

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