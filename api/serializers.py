from christmas_list.models import WishList, Item, Pledge
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        read_only_fields = ('id', )


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ('id', 'user', 'title', 'expiration', 'created_at')
        read_only_fields = ('id', 'user', 'created_at')


class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = ('id', 'user', 'item', 'amount', 'pledged_at')
        read_only_fields = ('id', 'user', 'pledged_at')


class ItemSerializer(serializers.ModelSerializer):
    pledge_set = PledgeSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'wish_list', 'title', 'description', 'price',
                  'source_url', 'image_url', 'created_at', 'pledge_set',
                  'total_pledged', 'amount_needed')
        read_only_fields = ('id', 'created_at', 'total_pledged',
                            'amount_needed')
