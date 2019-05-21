# article/serializers.py
from rest_framework import serializers
from articles import models

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ('author', 'title', 'created', 'content')

class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        liked_user = serializers.SlugRelatedField(source='liked_user', slug_field='name', read_only=True)

        fields = ('author', 'content', 'title', 'created', 'liked_users')