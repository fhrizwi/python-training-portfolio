from django.http import request,HttpResponse
from django.shortcuts import render

def home(request):
    return render (request,'home.html')
def about(request):
    # return HttpResponse("this is my about page")
    return render (request,'about.html')

def blog(request):
        return render (request,'blog.html')


def contact(request):
        return render (request,'contact.html')

