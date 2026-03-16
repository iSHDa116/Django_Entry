from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def show_hello(request):
    if(request.method == 'GET'):
        print('GETだぜ!!')
    return HttpResponse("Hello, Django")