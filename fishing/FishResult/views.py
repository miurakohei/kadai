from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse
from django.template import RequestContext
from FishResult.models import *
from FishResult.forms import *
def toppage(request):
    """トップページ"""
    return render(request,'FishResult/toppage.html')


def tools_list(request):
    """道具一覧"""
    rodlist = rod_master.objects.all().order_by('rod_id')
    return render(request,
                'FishResult/tools_list.html',
                {'rod' : rodlist})


def set_list(rerquest):
    """セット一覧"""
    return render(request,'FishResult/set_list.html')


def fishing_registration(request):
    """釣果登録"""
    return render(request,'FishResult/fishing_registration.html')


def map(request):
    """マップ画面"""
    return render(request,'FishResult/map.html')


def album(request):
    """アルバム画面"""
    return render(request,'FishResult/album.html')


def tools_edit(request, product_id=None):
    """道具追加"""
    if product_id:
        product = get_object_or_404(product_master, pk=puroduct_id)
    else:
        product=product_master()

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            procuct = form.save(commit=False)
            product.save()
            return redirect('FishResult:tools_list')
    else:
        form=ProductForm(instance=product)

    return render(request,'FishResult/tools_add.html', dict(form=form, product_id=product_id))
