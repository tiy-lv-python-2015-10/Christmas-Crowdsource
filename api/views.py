from api.serializers import UserSerializer, WishListSerializer, ItemSerializer, \
    PledgeSerializer
from christmas_list.models import WishList, Item, Pledge
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics


class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListWishLists(generics.ListAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer


class ListItems(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ListPledges(generics.ListAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer


class DetailUpdateWishList(generics.RetrieveUpdateDestroyAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer


class DetailUpdateItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class DetailUpdatePledge(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer