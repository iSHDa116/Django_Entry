from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

def show_hello(request):
    if(request.method == 'GET'):
        print('GETだぜ!!')
    return HttpResponse("Hello, Django")