from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views


urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
