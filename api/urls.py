from api.views import ListUsers, DetailUpdatePledge, DetailUpdateItem, \
    DetailUpdateWishList, ListCreatePledges, ListCreateItems, ListCreateWishLists, \
    CreateUser
from django.conf.urls import url
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^users/$', ListUsers.as_view(), name='api_list_users'),
    url(r'^users/create/$', CreateUser.as_view(), name='api_create_user'),
    url(r'^wishlists/$', ListCreateWishLists.as_view(),
        name='api_list_create_wishlists'),
    url(r'^items/$', ListCreateItems.as_view(), name='api_list_create_items'),
    url(r'^pledges/$', ListCreatePledges.as_view(),
        name='api_list_create_pledges'),
    url(r'^wishlists/(?P<pk>\d+)', DetailUpdateWishList.as_view(),
        name='api_detail_update_wishlist'),
    url(r'^items/(?P<pk>\d+)', DetailUpdateItem.as_view(),
        name='api_detail_update_item'),
    url(r'^pledges/(?P<pk>\d+)', DetailUpdatePledge.as_view(),
        name='api_detail_update_pledge'),
    url(r'^api-token-auth/$', views.obtain_auth_token)
]