from django.contrib import admin
from FishResult.models import  *


# admin.site.register(rod_master)
# admin.site.register(reel_master)
# admin.site.register(line_master)
# admin.site.register(rure_master)
# admin.site.register(worm_master)
# admin.site.register(gimmic_master)
# admin.site.register(maker_master)
# admin.site.register(use_master)
# admin.site.register(user_master)
# admin.site.register(product_master)
# admin.site.register(set_master)
# admin.site.register(ownership_master)
# admin.site.register(val_info_master)
# admin.site.register(fish_result)

class RodAdmin(admin.ModelAdmin):
    list_display = ('rod_id', 'rod_name','length')
    list_display_links = ['rod_id']
admin.site.register(rod_master, RodAdmin)


class ReelAdmin(admin.ModelAdmin):
    list_display = ('reel_id','reel_name', 'wind_length', 'weight')
    list_display_links = ['reel_id']
admin.site.register(reel_master, ReelAdmin)


class LineAdmin(admin.ModelAdmin):
    list_display = ('line_id','line_name', 'type_size')
    list_display_links = ['line_id']
admin.site.register(line_master, LineAdmin)


class RureAdmin(admin.ModelAdmin):
    list_display = ('rure_id','rure_name', 'weight')
    list_display_links = ['rure_id']
admin.site.register(rure_master, RureAdmin)


class WormAdmin(admin.ModelAdmin):
    list_display = ('worm_id','worm_name', 'inchi')
    list_display_links = ['worm_id']
admin.site.register(worm_master, WormAdmin)


class GimmicAdmin(admin.ModelAdmin):
    list_display = ('gimmic_id','gimmic_name')
    list_display_links = ['gimmic_id']
admin.site.register(gimmic_master, GimmicAdmin)


class MakerAdmin(admin.ModelAdmin):
    list_display = ('maker_id', 'maker_name')
    list_display_links = ['maker_id']
admin.site.register(maker_master, MakerAdmin)


class UseAdmin(admin.ModelAdmin):
    list_display = ('use_id', 'use_name', 'remarks')
    list_display_links = ['use_id']
admin.site.register(use_master, UseAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'use_id', 'create_date', 'image', 'classification', 'user_id')
    list_display_links = ['product_id']
admin.site.register(product_master, ProductAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name')
    list_display_links = ['user_id']
admin.site.register(user_master, UserAdmin)

class FishResultAdmin(admin.ModelAdmin):
    list_display = ('result_id','set_id','comment',
                    'latitude','longitude','create_time',
                    'image','user')
    list_display_links = ['result_id']
admin.site.register(fish_result, FishResultAdmin)
