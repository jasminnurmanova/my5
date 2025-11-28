from django.urls import path
from .views import client1,client2

urlpatterns=[
    path('client1/',client1),
    path('client2/', client2)
]