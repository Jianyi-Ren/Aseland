# Comments/serializers.py
from rest_framework import serializers
from comments import models

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment

        liked_user = serializers.SlugRelatedField(source='liked_user', slug_field='name', read_only=True)

        fields = (
            'created',
            'updated',
            'author',
            'article_id',
            'content',
            'liked_user'
        )

class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = (
            'created',
            'updated',
            'author',
            'article_id',
            'content'
        )
