# users/views.py
from rest_framework import generics, filters, permissions
import django_filters
from articles.v1 import serializers
from articles import models
from comments.v1.serializers import CommentSerializer
from comments.models import  Comment

class ArticleFilter(django_filters.FilterSet):
    class Meta:
        model = models.Article
        fields = (
            'author',
        )


class ArticleListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.ArticleSerializer
    filter_backends = (filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend)
    filter_class = ArticleFilter

    def get_queryset(self):
        qs = models.Article.objects.all()

        if self.request.query_params.get('pk'):
            pks = self.request.query_params.get('pk').split(",")
            qs = qs.filter(pk__in=pks)

        return qs


class ArticleGetModifyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.ArticleDetailSerializer

    def get_queryset(self):
        return models.Article.objects.filter(pk=self.kwargs['pk'])


class ArticleCommentListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(source_article=self.kwargs['pk'])