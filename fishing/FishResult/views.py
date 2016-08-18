from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse
from django.template import RequestContext
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory
from FishResult.models import *
from FishResult.forms import *


def toppage(request):
    """トップページ"""
    return render(request,'FishResult/toppage.html')


def tools_list(request):
    """道具一覧"""
    productlist = product_master.objects.all().order_by('classification')
    return render(request,
                'FishResult/tools_list.html',
                {'productlist' : productlist})


def tools_list_rod(request):
    """ロッド一覧"""
    productlist = product_master.objects.filter(classification=1).order_by('product_id')
    rodlist = rod_master.objects.all().order_by('rod_id')
    return render(request,
                'FishResult/tools_list_rod.html',
                {'productlist': productlist,
                 'rodlist': rodlist})


def tools_list_reel(request):
    """リール一覧"""
    productlist = product_master.objects.filter(classification=2).order_by('product_id')
    reellist = reel_master.objects.all().order_by('reel_id')
    return render(request,
                'FishResult/tools_list_reel.html',
                {'productlist': productlist,
                 'reellist' : reellist})


def tools_list_line(request):
    """ライン一覧"""
    productlist = product_master.objects.filter(classification=3).order_by('product_id')
    return render(request,
                'FishResult/tools_list_line.html',
                {'productlist': productlist})


def tools_list_rure(request):
    """ルアー一覧"""
    productlist = product_master.objects.filter(classification=4).order_by('product_id')
    return render(request,
                'FishResult/tools_list_rure.html',
                {'productlist': productlist})


def tools_list_worm(request):
    """ワーム一覧"""
    productlist = product_master.objects.filter(classification=5).order_by('product_id')
    return render(request,
                'FishResult/tools_list_worm.html',
                {'productlist': productlist})


def tools_list_gimmic(request):
    """仕掛け一覧"""
    productlist = product_master.objects.filter(classification=6).order_by('product_id')
    return render(request,
                'FishResult/tools_list_gimmic.html',
                {'productlist': productlist})


def set_list(request):
    """セット一覧"""
    setlist = set_master.objects.all().order_by('set_id')
    return render(request,
                'FishResult/set_list.html',
                {'setlist': setlist},)



def map(request):
    """マップ画面"""
    return render(request,'FishResult/map.html')


def form_map(request):
    """フォーム用map表示"""
    return render(request,'FishResult/form_map.html')


def album(request):
    """アルバム画面"""
    return render(request,'FishResult/album.html')


# def tools_edit(request, product_id=None):
#     """道具追加、編集"""
#     if product_id:
#         product = get_object_or_404(product_master, pk=product_id)
#     else:
#         product=product_master()
#
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.save()
#             return redirect('FishResult:tools_list')
#     else:
#         form=ProductForm(instance=product)
#
#     return render(request,'FishResult/tools_add.html', dict(form=form,  product_id=product_id))


def rod_edit(request, product_id=None):
    """ロッド追加,編集"""
    if product_id:
        rod = get_object_or_404(rod_master, pk=product_id)
        product = get_object_or_404(product_master, pk=product_id)
    else:
        product = product_master()
        rod = rod_master()

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, prefix='product',instance = product )
        rod_form = RodForm(request.POST, request.FILES, prefix='rod', instance = rod)
        if product_form.is_valid() & rod_form.is_valid():
            product = product_form.save(commit=False)
            rod = rod_form.save(commit=False)
            product.save()
            rod.rod_id = product.product_id
            rod.rod_name = product.product_name
            rod.save()
            return redirect('FishResult:tools_list_rod')
    else:
        rod_form = RodForm( prefix = 'rod', instance = rod)
        product_form = ProductForm(prefix = 'product', instance = product, initial = {
        'classification': 1 })
    return render(request,'FishResult/rod_add.html', dict(productform=product_form,
                                                            classificationform=rod_form,
                                                            product_id=product_id,
                                                            ))


def reel_edit(request, product_id=None):
    """リール追加,編集"""
    if product_id:
        reel = get_object_or_404(reel_master, pk=product_id)
        product = get_object_or_404(product_master, pk=product_id)
    else:
        product = product_master()
        reel = reel_master()

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, prefix='product',instance = product )
        reel_form = ReelForm(request.POST, request.FILES, prefix='reel', instance = reel)
        if product_form.is_valid() & reel_form.is_valid():
            product = product_form.save(commit=False)
            reel = reel_form.save(commit=False)
            product.save()
            reel.reel_id = product.product_id
            reel.reel_name = product.product_name
            reel.save()
            return redirect('FishResult:tools_list_reel')
    else:
        reel_form = ReelForm( prefix = 'reel', instance = reel)
        product_form = ProductForm(prefix = 'product', instance = product, initial = {
        'classification': 2 })
    return render(request,'FishResult/reel_add.html', dict(productform=product_form,
                                                            classificationform=reel_form,
                                                            product_id=product_id,
                                                            ))


def line_edit(request, product_id=None):
    """ライン追加,編集"""
    if product_id:
        line = get_object_or_404(line_master, pk=product_id)
        product = get_object_or_404(product_master, pk=product_id)
    else:
        product = product_master()
        line = line_master()

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, prefix='product',instance = product )
        line_form = LineForm(request.POST, request.FILES, prefix='line', instance = line)
        if line_form.is_valid() & product_form.is_valid():
            product = product_form.save(commit=False)
            line = line_form.save(commit=False)
            product.save()
            line.line_id = product.product_id
            line.line_name = product.product_name
            line.save()
            return redirect('FishResult:tools_list_line')
    else:
        line_form = LineForm( prefix = 'line', instance = line)
        product_form = ProductForm(prefix = 'product', instance = product, initial = {
        'classification': 3 })
    return render(request,'FishResult/line_add.html', dict(productform=product_form,
                                                            classificationform=line_form,
                                                            product_id=product_id,
                                                            ))


def rure_edit(request, product_id=None):
    """ルアー追加,編集"""
    if product_id:
        rure = get_object_or_404(rure_master, pk=product_id)
        product = get_object_or_404(product_master, pk=product_id)
    else:
        product = product_master()
        rure = rure_master()

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, prefix='product',instance = product )
        rure_form = RureForm(request.POST, request.FILES, prefix='rure', instance = rure)
        if rure_form.is_valid() & product_form.is_valid():
            product = product_form.save(commit=False)
            rure = rure_form.save(commit=False)
            product.save()
            rure.rure_id = product.product_id
            rure.rure_name = product.product_name
            rure.save()
            return redirect('FishResult:tools_list_rure')
    else:
        rure_form = RureForm( prefix = 'rure', instance = rure)
        product_form = ProductForm(prefix = 'product', instance = product, initial = {
        'classification': 4 })
    return render(request,'FishResult/rure_add.html', dict(productform=product_form,
                                                            classificationform=rure_form,
                                                            product_id=product_id,
                                                            ))


def gimmic_edit(request, product_id=None):
    """仕掛け追加,編集"""
    if product_id:
        gimmic = get_object_or_404(gimmic_master, pk=product_id)
        product = get_object_or_404(product_master, pk=product_id)
    else:
        product = product_master()
        gimmic = gimmic_master()

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, prefix='product',instance = product)
        gimmic_form = GimmicForm(request.POST, request.FILES, prefix='gimmic', instance = gimmic)
        if gimmic_form.is_valid() & product_form.is_valid():
            product = product_form.save(commit=False)
            gimmic = gimmic_form.save(commit=False)
            product.save()
            gimmic.gimmic_id = product.product_id
            gimmic.gimmic_name = product.product_name
            gimmic.save()
            return redirect('FishResult:tools_list_gimmic')
    else:
        gimmic_form = GimmicForm( prefix = 'gimmic', instance = gimmic)
        product_form = ProductForm(prefix = 'product', instance = product,  initial = {
        'classification': 6 })
    return render(request,'FishResult/gimmic_add.html', dict(productform=product_form,
                                                            classificationform=gimmic_form,
                                                            product_id=product_id,
                                                            ))

def worm_edit(request, product_id=None):
    """ワーム追加,編集"""
    if product_id:
        worm = get_object_or_404(worm_master, pk=product_id)
        product = get_object_or_404(product_master, pk=product_id)
    else:
        product = product_master()
        worm = worm_master()

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, prefix='product',instance = product)
        worm_form = WormForm(request.POST, request.FILES, prefix='worm', instance = worm)
        if worm_form.is_valid() & product_form.is_valid():
            product = product_form.save(commit=False)
            worm = worm_form.save(commit=False)
            product.save()
            worm.worm_id = product.product_id
            worm.worm_name = product.product_name
            worm.save()
            return redirect('FishResult:tools_list_worm')
    else:
        worm_form = WormForm( prefix = 'worm', instance = worm)
        product_form = ProductForm(prefix = 'product', instance = product,  initial = {
        'classification': 5 })
    return render(request,'FishResult/worm_add.html', dict(productform=product_form,
                                                            classificationform=worm_form,
                                                            product_id=product_id,
                                                            ))



def tools_del(request, product_id):
    """道具の削除"""
    product = get_object_or_404(product_master, pk=product_id)
    if product.classification == '1':
        rod = get_object_or_404(rod_master, pk=product_id)
        rod.delete()
    if product.classification == '2':
        reel = get_object_or_404(reel_master, pk=product_id)
        reel.delete()
    if product.classification == '3':
        line = get_object_or_404(line_master, pk=product_id)
        line.delete()
    if product.classification == '4':
        rure = get_object_or_404(rure_master, pk=product_id)
        rure.delete()
    if product.classification == '5':
        worm = get_object_or_404(worm_master, pk=product_id)
        worm.delete()
    if product.classification == '6':
        gimmic = get_object_or_404(gimmic_master, pk=product_id)
        gimmic.delete()
    product.delete()
    return redirect('FishResult:tools_list')


def set_edit(request, set_id=None):
    """セット追加、編集"""
    if set_id:
        set = get_object_or_404(set_master, pk=set_id)
    else:
        set=set_master()

    if request.method == 'POST':
        form = SetForm(request.POST, instance=set)
        if form.is_valid():
            set = form.save(commit=False)
            set.save()
            return redirect('FishResult:set_list')
    else:
        form=SetForm(instance=set)

    return render(request,'FishResult/set_add.html', dict(form=form, set_id=set_id))


def set_del(request, set_id):
    """セットの削除"""
    set = get_object_or_404(set_master, pk=set_id)
    set.delete()
    return redirect('FishResult:set_list')


def result_edit(request, result_id=None):
    """釣果追加、編集"""
    if result_id:
        result = get_object_or_404(fish_result, pk=result_id)
    else:
        result = fish_result()

    if request.method == 'POST':
        form = ResultForm(request.POST, instance=result)
        if form.is_valid():
            result = form.save(commit=False)
            result.save()
            return redirect('FishResult:top')
    else:
        form=ResultForm(instance=result)

    return render(request,'FishResult/fishing_registration.html', dict(form=form, result_id=result_id))
