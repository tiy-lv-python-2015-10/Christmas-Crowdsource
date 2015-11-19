from christmas_list.models import WishList, Item, Pledge
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('id', )


    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


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
