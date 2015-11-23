from christmas_list.models import WishList, Item, Pledge
from django.contrib import admin

@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'expiration', 'is_expired',
                    'created_at')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'wish_list', 'title', 'description', 'price',
                    'source_url', 'image_url', 'is_funded',
                    'is_closed', 'created_at')

@admin.register(Pledge)
class PledgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'item', 'amount', 'charge_id',
                    'is_refunded', 'pledged_at')