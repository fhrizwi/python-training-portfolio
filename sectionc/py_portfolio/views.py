from django.shortcuts import render
from django.http import request,HttpResponse

def hello(request):
    # return HttpResponse("Hello, world. You're at the portfolio index.")
    return render (request, 'maggii/hello.html')

def tom(request):
    return HttpResponse("here is my all blogs.")
# Create your views here.
