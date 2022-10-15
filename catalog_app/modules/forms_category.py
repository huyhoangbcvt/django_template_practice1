from ..models.category_model import Category
from ..models.product_model import Product
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class CatalogForm(forms.ModelForm):
    def __init__(self, *args, user=None, product=None, **kwargs):
        super(CatalogForm, self).__init__(*args, **kwargs)
        if user is not None and not user.is_superuser:
            self.fields['user'].queryset = User.objects.filter(username=user.username)
        if product is not None:
            self.fields['product_map'].queryset = product

    class Meta:
        # model = Product
        model = Category
        # model['product'] = forms.ChoiceField(label="Chọn sản phẩm", choices=Product.objects.all())
        fields = ['title', 'image', 'content', 'product_map', 'user']
        labels = {'title': _('Tiêu đề'), 'image': _('Hình ảnh category'), 'content': _('Nội dung'),
                  'product_map': _('Chọn sản phẩm'), 'user': _('Tài khoản tạo')}


