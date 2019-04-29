# users/views.py
from rest_framework import generics, filters
import django_filters
from django_filters.filters import ChoiceFilter
from Aseland.users import models
from Aseland.users.v1 import serializers
from Aseland.users.static import UserConstants




class UserFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(name="name", lookup_expr='icontains')

    min_birthday = django_filters.IsoDateTimeFilter(name="birthday", lookup_expr='gte')
    max_birthday = django_filters.IsoDateTimeFilter(name="birthday", lookup_expr='lte')

    status = ChoiceFilter(choices=UserConstants.USER_STATUS_CHOICES)
    gender = ChoiceFilter(choices=UserConstants.USER_GENDER_CHOICES)
    province = django_filters.CharFilter(name="name", lookup_expr='icontains')
    city = django_filters.CharFilter(name="name", lookup_expr='icontains')

    sex_acceptance = ChoiceFilter(choices=UserConstants.USER_SEX_ACCEPTANCE_CHOICES)
    marriage_status = ChoiceFilter(choices=UserConstants.USER_MARRIAGE_STATUS_CHOICES)
    education = ChoiceFilter(choices=UserConstants.USER_EDUCATION_CHOICES)

    class Meta:
        model = UserListView
        fields = [
            'name', 'status', 'gender',  'min_birthday', 'max_birthday',
            'province', 'city', 'sex_acceptance', 'marriage_status', 'education'
        ]

class UserListView(generics.ListCreateAPIView):

    serializer_class = serializers.UserSerializer
    filter_backends = (filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend)

    filter_class = UserFilter

    def get_queryset(self):
        queryset = models.CustomUser.objects.all()
        return queryset
