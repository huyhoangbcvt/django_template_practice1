from ..models.product_model import Product
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['p_title', 'p_name', 'p_code', 'p_image', 'p_description', 'p_country', 'author']