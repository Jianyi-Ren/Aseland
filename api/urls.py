# api/urls.py
from django.urls import include, path

urlpatterns = [
    path('users/', include('users.v1.urls')),
    path('comments/', include('comments.v1.urls')),
    path('articles/', include('articles.v1.urls')),

    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
