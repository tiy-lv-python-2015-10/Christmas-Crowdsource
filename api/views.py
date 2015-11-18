from api.serializers import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics


class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
