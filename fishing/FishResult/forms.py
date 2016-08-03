from django.forms import ModelForm
from FishResult.models import *


class ProductForm(ModelForm):
    """商品フォーム"""
    class Meta:
        model=product_master
        fields = ('product_id', 'product_name', 'maker_id', 'use_id','image', 'classification', 'user_id')
