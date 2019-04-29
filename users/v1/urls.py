# users/urls.py
from django.urls import path

from Aseland.users.v1 import views

urlpatterns = [

    path('', views.UserListView.as_view()),


    # get user list

    # get a user detail

    # update user detail


    

    # Friend

    # save a user

    # block a user




]