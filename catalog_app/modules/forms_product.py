from ..models.product_model import Product
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class ProductForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        if user is not None and not user.is_superuser:
            self.fields['user'].queryset = User.objects.filter(username=user.username)

    class Meta:
        model = Product
        fields = ['p_title', 'p_name', 'p_code', 'p_image', 'p_description', 'p_country', 'middles', 'user']
        labels = {'p_title': _('Tiêu đề'), 'p_name': _('Tên sản phẩm'), 'p_code': _('Mã sản phẩm'),
                  'p_description': _('Mô tả sản phẩm'), 'p_country': _('Xuất xứ'), 'image': _('Hình ảnh Category'),
                  'middles': _('Chọn Category (*)'), 'user': _('Tài khoản tạo')}