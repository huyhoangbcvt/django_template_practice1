from ..models.category_model import Category
from django import forms

class CatalogForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'image', 'content', 'product']