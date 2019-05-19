# articles/urls.py
from django.urls import include, path
from . import views

urlpatterns = [

    path('', views.ArticleListView.as_view()),
    path('<int:pk>', views.ArticleGetModifyView.as_view()),

    ]
