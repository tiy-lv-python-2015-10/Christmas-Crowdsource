from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from django.conf.urls import include

urlpatterns = [

    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'api/api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
