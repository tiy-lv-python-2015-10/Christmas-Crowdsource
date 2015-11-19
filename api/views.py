from api import permissions
from christmas_lists.models import WishList, Item, Pledge
from django.db.models import Count
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, permissions, filters
from rest_framework.throttling import AnonRateThrottle
from api.permissions import IsOwnerOrReadOnly
from api.serializers import WishlistSerializer, ItemSerializer, PledgeSerializer


class SmallPagination(PageNumberPagination):
    page_size = 50


class APIListCreateWishList(generics.ListCreateAPIView):
    queryset = WishList.objects.order_by('-created_at')
    serializer_class = WishlistSerializer
    pagination_class = SmallPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    # search_fields = ('posting_title', 'specific_location', 'posting_body')

    def perform_create(self, serializer):
        serializer.save()


class APIDetailUpdateWishList(generics.RetrieveUpdateDestroyAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)





class APIListCreateItem(generics.ListCreateAPIView):
    queryset = Item.objects.order_by('-created_at')
    serializer_class = ItemSerializer
    pagination_class = SmallPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    # search_fields = ('posting_title', 'specific_location', 'posting_body')

    def perform_create(self, serializer):
        serializer.save()


class APIDetailUpdateItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)





class APIListCreatePledge(generics.ListCreateAPIView):
    queryset = Pledge.objects.order_by('-created_at')
    serializer_class = PledgeSerializer
    pagination_class = SmallPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    # search_fields = ('posting_title', 'specific_location', 'posting_body')

    def perform_create(self, serializer):
        serializer.save()


class APIDetailUpdatePledge(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)