from django.urls import path
from .views import book1,book2

urlpatterns=[
    path('book1/',book1),
    path('book2/', book2)
]