from api.views import ListUsers, DetailUpdatePledge, DetailUpdateItem, \
    DetailUpdateWishList, ListPledges, ListItems, ListWishLists
from django.conf.urls import url

urlpatterns = [
    url(r'^users/$', ListUsers.as_view()),
    url(r'^wishlists/$', ListWishLists.as_view()),
    url(r'^items/$', ListItems.as_view()),
    url(r'^pledges/$', ListPledges.as_view()),
    url(r'^wishlists/(?P<pk>\d+)', DetailUpdateWishList.as_view()),
    url(r'^items/(?P<pk>\d+)', DetailUpdateItem.as_view()),
    url(r'^pledges/(?P<pk>\d+)', DetailUpdatePledge.as_view()),
]
