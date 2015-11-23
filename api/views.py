import os
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
import stripe


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
       user = self.request.user
       serializer.save(user=user)




class APIDetailUpdateWishList(generics.RetrieveUpdateDestroyAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = (IsOwnerOrReadOnly,)





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
    permission_classes = (IsOwnerOrReadOnly,)





class APIListCreatePledge(generics.ListCreateAPIView):
    queryset = Pledge.objects.order_by('-created_at')
    serializer_class = PledgeSerializer
    pagination_class = SmallPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    # search_fields = ('posting_title', 'specific_location', 'posting_body')


    def perform_create(self, serializer):
        stripe.api_key = os.environ('STRIPE_API_KEY')
        token = serializer.initial_data['token']

        try:
           charge = stripe.Charge.create(
               amount=serializer.initial_data['amount'],
               currency="usd",
               source=token,
               description="Pledge"
           )
           charge_id = charge['id']
        except stripe.error.CardError:
           pass



        serializer.save(charge_id=charge_id)

    def get_queryset(self):
        qs = super().get_queryset()
        username = self.request.query_params.get('username', None)
        if username:
           qs = qs.filter(user__username=username)
        return qs












    # def perform_create(self, serializer):
    #     user = self.request.user
    #     serializer.save(user=user)


class APIDetailUpdatePledge(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    permission_classes = (IsOwnerOrReadOnly,)