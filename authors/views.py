from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def author1(request):
    return HttpResponse('Steven King')

def author2(request):
    return HttpResponse('Pushkin')