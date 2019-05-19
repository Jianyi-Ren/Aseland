# article/serializers.py
from rest_framework import serializers
from articles import models

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ('author', 'content')

class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ('author', 'content')