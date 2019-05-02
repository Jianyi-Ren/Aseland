# users/views.py
from rest_framework import generics, filters, permissions
import django_filters
from django_filters.filters import ChoiceFilter
from users import models
from users.v1 import serializers
from users.static import UserConstants



class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')

    min_birthday = django_filters.IsoDateTimeFilter(field_name="birthday", lookup_expr='gte')
    max_birthday = django_filters.IsoDateTimeFilter(field_name="birthday", lookup_expr='lte')

    status = ChoiceFilter(choices=UserConstants.USER_STATUS_CHOICES)
    gender = ChoiceFilter(choices=UserConstants.USER_GENDER_CHOICES)
    province = django_filters.CharFilter(field_name="province", lookup_expr='icontains')
    city = django_filters.CharFilter(field_name="city", lookup_expr='icontains')

    sex_acceptance = ChoiceFilter(choices=UserConstants.USER_SEX_ACCEPTANCE_CHOICES)
    marriage_status = ChoiceFilter(choices=UserConstants.USER_MARRIAGE_STATUS_CHOICES)
    education = ChoiceFilter(choices=UserConstants.USER_EDUCATION_CHOICES)

    class Meta:
        model = models.CustomUser
        fields = (
            'username', 'status',
        )

class UserListView(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.UserSerializer
    filter_backends = (filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend)
    filter_class = UserFilter

    def get_queryset(self):
        qs =  models.CustomUser.objects.all()

        if self.request.query_params.get('pk'):
            pks = self.request.query_params.get('pk').split(",")
            qs = qs.filter(pk__in=pks)

        return qs


class UserGetModifyView(generics.RetrieveAPIView, generics.UpdateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    print('UserGetModifyView')
    serializer_class = serializers.UserDetailSerializer

    def get_queryset(self):
        return models.CustomUser.objects.filter(pk=self.kwargs['pk'])
