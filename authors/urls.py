from django.urls import path
from .views import author1,author2

urlpatterns=[
    path('author1/',author1),
    path('author2/', author2)
]