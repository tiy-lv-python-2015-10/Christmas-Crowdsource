from christmas_list.models import WishList, Item, Pledge
from django.contrib.auth.models import User
from rest_framework import serializers
from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('user',)


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('id', )

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        profile_data = validated_data.pop('profile')
        profile = Profile.objects.create(
            user=user,
            first_name=profile_data.get('first_name', None),
            last_name=profile_data.get('last_name', None),
            address=profile_data.get('address', None),
            address_2=profile_data.get('address_2', None),
            city=profile_data.get('city', None),
            state=profile_data.get('state', None),
            zip=profile_data.get('zip', None)
        )
        return user

class ShortItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'title', 'price', 'image_url', 'total_pledged',
                  'amount_needed')
        read_ony_fields = ('__all__')

class PledgeSerializer(serializers.ModelSerializer):
    item = ShortItemSerializer(many=False)

    class Meta:
        model = Pledge
        fields = ('id', 'user', 'item', 'amount')
        read_only_fields = ('id', 'user')


class WishListSerializer(serializers.ModelSerializer):
    item_set = ShortItemSerializer(many=True, read_only=True)

    class Meta:
        model = WishList
        fields = ('id', 'user', 'title', 'expiration', 'item_set')
        read_only_fields = ('id', 'user', 'item_set')


class ItemSerializer(serializers.ModelSerializer):
    pledge_set = PledgeSerializer(many=True, read_only=True)
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.wish_list.user.username

    class Meta:
        model = Item
        fields = ('id', 'wish_list', 'user', 'title', 'description', 'price',
                  'source_url', 'image_url', 'pledge_set',
                  'total_pledged', 'amount_needed')
        read_only_fields = ('id', 'total_pledged',
                            'amount_needed')