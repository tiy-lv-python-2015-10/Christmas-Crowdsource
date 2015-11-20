from api.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from api.serializers import UserSerializer, WishListSerializer, ItemSerializer, \
    PledgeSerializer
from christmas_list.models import WishList, Item, Pledge
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics


class ListUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListWishLists(generics.ListCreateAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class ListItems(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class ListPledges(generics.ListCreateAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class DetailUpdateWishList(generics.RetrieveUpdateDestroyAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


class DetailUpdateItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


class DetailUpdatePledge(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

