from django.conf.urls import url, include
from FishResult import views
from django.conf import settings

urlpatterns = [
    url(r'^static(?P<path>.*)$','django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}),
    url(r'^top/$', views.toppage, name='toppage'),
    url(r'^top/tools_list/$', views.tools_list, name='tools_list'),
    url(r'^top/set_list/$', views.set_list, name='set_list'),
    url(r'^top/fishing_registration/$', views.fishing_registration, name='fishing_registration'),
    url(r'^top/map/$', views.map, name='map'),
    url(r'^top/album/$', views.album, name='album'),
    url(r'^top/tools_add/$', views.tools_edit, name='tools_add'),
    url(r'^top/tools_mod/(?P<product_id>\d+)$', views.tools_edit, name='tools_mod'),
    ]
