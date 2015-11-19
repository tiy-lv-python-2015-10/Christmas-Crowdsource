from django.contrib import admin
from christmas_lists.models import WishList, Item, Pledge


@admin.register(WishList)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('title','list_url','expiration_date','user', 'created_at', 'modified_at')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('wish_list','item_url','image_url','title','description','price', 'created_at', 'modified_at')

@admin.register(Pledge)
class PledgeAdmin(admin.ModelAdmin):
    list_display = ('user','item', 'pledge_amount','created_at', 'modified_at')
# Register your models here.
