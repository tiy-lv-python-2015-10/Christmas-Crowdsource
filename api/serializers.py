from django.contrib.auth.models import User
from rest_framework import serializers
from christmas_lists.models import WishList, Item, Pledge

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ('title','list_url', 'expiration_date', 'user', 'created_at', 'modified_at')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('wish_list', 'item_url', 'image_url', 'title', 'description', 'price',
                  'pledge_total', 'created_at', 'modified_at')


class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = ('user', 'item', 'pledge_amount', 'created_at', 'modified_at')