from django.conf.urls import url, include
from FishResult import views
from django.conf import settings

urlpatterns = [
    url(r'^media(?P<path>.*)$','django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}),
    url(r'^top/$', views.toppage, name='toppage'),
    #　道具リスト
    url(r'^top/tools_list/$', views.tools_list, name='tools_list'),
    url(r'^top/tools_list_rod/$', views.tools_list_rod, name='tools_list_rod'),
    url(r'^top/tools_list_reel/$', views.tools_list_reel, name='tools_list_reel'),
    url(r'^top/tools_list_line/$', views.tools_list_line, name='tools_list_line'),
    url(r'^top/tools_list_rure/$', views.tools_list_rure, name='tools_list_rure'),
    url(r'^top/tools_list_worm/$', views.tools_list_worm, name='tools_list_worm'),
    url(r'^top/tools_list_gimmic/$', views.tools_list_gimmic, name='tools_list_gimmic'),
    #　セットリスト
    url(r'^top/set_list/$', views.set_list, name='set_list'),
    url(r'^top/map/$', views.map, name='map'),
    url(r'^top/album/$', views.album, name='album'),
    # 各道具の追加、編集
    url(r'^top/tools_rod_add/$', views.rod_edit, name='rod_add'),
    url(r'^top/tools_rod_mod/(?P<product_id>\d+)$', views.rod_edit, name='rod_mod'),
    url(r'^top/tools_reel_add/$', views.reel_edit, name='reel_add'),
    url(r'^top/tools_reel_mod/(?P<product_id>\d+)$', views.reel_edit, name='reel_mod'),
    url(r'^top/tools_line_add/$', views.line_edit, name='line_add'),
    url(r'^top/tools_line_mod/(?P<product_id>\d+)$', views.line_edit, name='line_mod'),
    url(r'^top/tools_rure_add/$', views.rure_edit, name='rure_add'),
    url(r'^top/tools_rure_mod/(?P<product_id>\d+)$', views.rure_edit, name='rure_mod'),
    url(r'^top/tools_gimmic_add/$', views.gimmic_edit, name='gimmic_add'),
    url(r'^top/tools_gimmic_mod/(?P<product_id>\d+)$', views.gimmic_edit, name='gimmic_mod'),
    url(r'^top/tools_worm_add/$', views.worm_edit, name='worm_add'),
    url(r'^top/tools_worm_mod/(?P<product_id>\d+)$', views.worm_edit, name='worm_mod'),
    # 道具削除
    url(r'^top/tools_del/(?P<product_id>\d+)$', views.tools_del, name='tools_del'),
    #　セット追加削除編集
    url(r'^top/set_add/$', views.set_edit, name='set_add'),
    url(r'^top/set_mod/(?P<set_id>\d+)$', views.set_edit, name='set_mod'),
    url(r'^top/set_del/(?P<set_id>\d+)$', views.set_del, name='set_del'),
    # 釣果登録編
    url(r'^top/fishing_registration/$', views.result_edit, name='fishing_registration'),
    url(r'^top/result_mod/$', views.result_edit, name='result_mod'),
    url(r'^top/form_map/$', views.form_map, name='form_map'),
    ]
