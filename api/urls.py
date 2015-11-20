from api.views import ListUsers, DetailUpdatePledge, DetailUpdateItem, \
    DetailUpdateWishList, ListCreatePledges, ListCreateItems, ListCreateWishLists, \
    CreateUser
from django.conf.urls import url
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^users/$', ListUsers.as_view()),
    url(r'^users/create/$', CreateUser.as_view()),
    url(r'^wishlists/$', ListCreateWishLists.as_view()),
    url(r'^items/$', ListCreateItems.as_view()),
    url(r'^pledges/$', ListCreatePledges.as_view()),
    url(r'^wishlists/(?P<pk>\d+)', DetailUpdateWishList.as_view()),
    url(r'^items/(?P<pk>\d+)', DetailUpdateItem.as_view()),
    url(r'^pledges/(?P<pk>\d+)', DetailUpdatePledge.as_view()),
    url(r'^api-token-auth/$', views.obtain_auth_token)
]