from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
   return render(request,'calculator.html')

def add(request):
   val1=int(request.GET['subtotal'])
   val2=int(request.GET['per'])
   res=int(val1*val2)/100
   total=val1+res
   return render(request,'result.html', {"result":total})