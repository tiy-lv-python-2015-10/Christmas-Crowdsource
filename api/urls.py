from api.views import APIDetailUpdateWishList, APIListCreateWishList, APIDetailUpdateItem, APIListCreateItem, \
    APIDetailUpdatePledge, APIListCreatePledge
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from django.conf.urls import include

urlpatterns = [

    url(r'^wishlists/(?P<pk>\d+)$', APIDetailUpdateWishList.as_view(), name='api_wishlist_detail_update'),
    url(r'^wishlists/$', APIListCreateWishList.as_view(), name='api_wishlist_list_create'),
    url(r'^items/(?P<pk>\d+)$', APIDetailUpdateItem.as_view(), name='api_item_detail_update'),
    url(r'^items/$', APIListCreateItem.as_view(), name='api_item_list_create'),
    url(r'^pledges/(?P<pk>\d+)$', APIDetailUpdatePledge.as_view(), name='api_pledge_detail_update'),
    url(r'^pledges/$', APIListCreatePledge.as_view(), name='api_pledge_list_create'),
    url(r'^api-token-auth/', views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
