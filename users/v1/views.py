# users/views.py
from rest_framework import generics

from Aseland.users import models
from Aseland.users.v1 import serializers


class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer