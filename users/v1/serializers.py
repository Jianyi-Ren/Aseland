# users/serializers.py
from rest_framework import serializers
from users import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser

        fields = (
            'name',
            'status',
            'gender',
            'birthday',
            'province',
            'city',
            'avatar',
            'sex_acceptance',
            'marriage_status',
            'education',
            'occupation',
            'signature'
        )

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        saved_users = serializers.SlugRelatedField(source='saved_users', slug_field='name', read_only=True)
        blocked_users = serializers.SlugRelatedField(source='blocked_users', slug_field='name', read_only=True)

        fields = (
            'name',
            'status',
            'gender',
            'birthday',
            'province',
            'city',
            'avatar',
            'sex_acceptance',
            'marriage_status',
            'education',
            'occupation',
            'signature'
        )