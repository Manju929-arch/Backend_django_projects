from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add(request):
    a = int(input("Enter a number 1 "))
    b = int(input("Enter the number 2 "))
    c = a+b
    return HttpResponse(str(c))

def sub(request):
    a = int(input("Enter a number 1 "))
    b = int(input("Enter the nubmer 2 "))
    c = a-b
    return HttpResponse(str(c))

def mul(request):
    a = int(input("Enter the number 1 "))
    b = int(input("Enter the number 2 "))
    c = a*b
    return HttpResponse(str(c))
