from api.views import ListUsers
from django.conf.urls import url

urlpatterns = [
    url(r'^users/', ListUsers.as_view())
]
