# Comments/views.py
from rest_framework import generics, filters, permissions
import django_filters
from django_filters.filters import ChoiceFilter
from comments import models
from comments.v1 import serializers



class CommentFilter(django_filters.FilterSet):
    article_id = django_filters.CharFilter(field_name="article_id")

    class Meta:
        model = models.Comment
        fields = [
            'article_id'
        ]

class CommentListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.CommentSerializer
    filter_backends = (filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend)
    filter_class = CommentFilter

    def get_queryset(self):
        qs =  models.Comment.objects.all()

        if self.request.query_params.get('pk'):
            pks = self.request.query_params.get('pk').split(",")
            qs = qs.filter(pk__in=pks)

        return qs


class CommentGetModifyView(generics.RetrieveAPIView, generics.UpdateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.CommentDetailSerializer

    def get_queryset(self):
        return models.Comment.objects.filter(pk=self.kwargs['pk'])

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)