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
