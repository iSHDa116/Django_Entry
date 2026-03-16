from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# @login_required
def show_hello(request):
    if(request.method == 'GET'):
        print('GETだぜ!!')
    return HttpResponse("Hello, Django")