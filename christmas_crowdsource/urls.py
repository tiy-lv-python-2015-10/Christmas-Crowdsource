"""christmas_crowdsource URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from api.views import APIDetailUpdateWishList, APIListCreateWishList, APIDetailUpdateItem, APIListCreateItem, \
    APIDetailUpdatePledge, APIListCreatePledge
from christmas_crowdsource import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken import views
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.cache import cache_page
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from django.conf.urls import include


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    # url(r'^login/', include('rest_framework.urls',namespace='rest_framework')),
    # url('^', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

