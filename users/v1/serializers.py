# users/serializers.py
from rest_framework import serializers
from Aseland.users import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username', )