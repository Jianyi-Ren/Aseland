# users/urls.py
from django.urls import include, path
from . import views

urlpatterns = [

    path('', views.UserListView.as_view()),
    path('<int:pk>', views.UserGetModifyView.as_view()),

    # get user list


    # get a user detail

    # update user detail


    # Friend

    # save a user

    # block a user




]
