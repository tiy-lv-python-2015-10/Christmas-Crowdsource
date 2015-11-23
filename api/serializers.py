from django.contrib.auth.models import User
from rest_framework import serializers
from christmas_lists.models import WishList, Item, Pledge

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        user = serializers.ReadOnlyField(source='user.id')
        fields = ('title','list_url', 'expiration_date','expired', 'user', 'created_at', 'modified_at')
        read_only_fields = ('user', 'created_at', 'modified_at', 'expired', 'created_at', 'modified_at')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('wish_list', 'reserved', 'item_url', 'image_url', 'title', 'description', 'price',
                  'pledge_total', 'created_at', 'modified_at')
        read_only_fields = ('pledge_total', 'created_at', 'modified_at')


class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        user = serializers.ReadOnlyField(source='user.id')
        fields = ('user', 'item', 'pledge_amount', 'created_at', 'modified_at')
        read_only_fields = ('user', 'created_at', 'modified_at')