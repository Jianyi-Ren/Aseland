# users/views.py
from rest_framework import generics, filters, permissions
import django_filters
from articles.v1 import serializers
from articles import models


class ArticleFilter(django_filters.FilterSet):
    class Meta:
        model = models.Article
        fields = (
            'author',
        )


class ArticleListView(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.ArticleSerializer
    filter_backends = (filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend)
    filter_class = ArticleFilter

    def get_queryset(self):
        qs = models.Article.objects.all()

        if self.request.query_params.get('pk'):
            pks = self.request.query_params.get('pk').split(",")
            qs = qs.filter(pk__in=pks)

        return qs


class ArticleGetModifyView(generics.RetrieveAPIView, generics.UpdateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.ArticleDetailSerializer

    def get_queryset(self):
        return models.Article.objects.filter(pk=self.kwargs['pk'])


