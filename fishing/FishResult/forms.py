from django.forms import ModelForm
from django import forms
from django.forms.formsets import formset_factory
from FishResult.models import *


class ProductForm(ModelForm):
    """商品フォーム"""
    class Meta:
        model=product_master
        fields = ('product_id', 'product_name',
                'maker_id', 'use_id','image',
                'classification', 'user_id')


class RodForm(ModelForm):
    """ロッドフォーム"""
    class Meta:
        model=rod_master
        exclude =('rod_id', 'rod_name')


class ReelForm(ModelForm):
    """リールフォーム"""
    class Meta:
        model=reel_master
        exclude =('reel_id', 'reel_name')


class LineForm(ModelForm):
    """ラインフォーム"""
    class Meta:
        model=line_master
        exclude =('line_id', 'line_name')


class RureForm(ModelForm):
    """ルアーフォーム"""
    class Meta:
        model=rure_master
        exclude =('rure_id', 'rure_name')


class GimmicForm(ModelForm):
    """仕掛けフォーム"""
    class Meta:
        model=gimmic_master
        exclude =('gimmic_id', 'gimmic_name')


class WormForm(ModelForm):
    """ワームフォーム"""
    class Meta:
        model=worm_master
        exclude =('worm_id', 'worm_name')


class SetForm(ModelForm):
    """セットふぉーむ"""
    class Meta:
        model=set_master
        fields = ('set_id', 'set_name',
                'rod_id', 'reel_id','line_id',
                'rure_id', 'worm_id',
                'gimmic_id', 'image',
                'user',)


class ResultForm(ModelForm):
    """釣果登録フォーム"""
    class Meta:
        model=fish_result
        fields = ('result_id', 'set_id',
                'comment',  'image', 'user',
                'latitude','longitude',)
