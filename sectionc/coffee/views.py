from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def all_coffee(request):
    return render(request,'newcoffee/coffee.html')

def orders(request):
    return render(request,'newcoffee/orders.html')



