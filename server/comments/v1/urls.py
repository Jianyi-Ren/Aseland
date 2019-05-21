# comments/urls.py
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.CommentListView.as_view()),
    path('<int:pk>', views.CommentGetModifyView.as_view()),

]
