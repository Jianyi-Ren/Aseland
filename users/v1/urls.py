# users/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [

    url('', views.UserListView.as_view()),


    # get user list
    url(r'^users/$',
        views.UserListView.as_view(), name='user-list'
        )

    # get a user detail

    # update user detail




    # Friend

    # save a user

    # block a user




]