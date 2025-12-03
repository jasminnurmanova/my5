from django.urls import path
from .views import client1,author2

urlpatterns=[
    path('client1/',client1),
    path('author2/', author2)
]