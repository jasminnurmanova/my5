from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def client1(request):
    return HttpResponse('Arthur')

def author2(request):
    return HttpResponse('Kolya')