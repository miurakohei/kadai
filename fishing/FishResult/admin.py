from django.contrib import admin
from FishResult.models import  (rod_master,
                                reel_master,
                                line_master,
                                rure_master,
                                worm_master,
                                gimmic_master,
                                maker_master,
                                use_master,
                                user_master,
                                product_master,
                                set_master,
                                ownership_master,
                                val_info_master,
                                fish_result,
                                )



admin.site.register(rod_master)
admin.site.register(reel_master)
admin.site.register(line_master)
admin.site.register(rure_master)
admin.site.register(worm_master)
admin.site.register(gimmic_master)
admin.site.register(maker_master)
admin.site.register(use_master)
admin.site.register(user_master)
admin.site.register(product_master)
admin.site.register(set_master)
admin.site.register(ownership_master)
admin.site.register(val_info_master)
admin.site.register(fish_result)
