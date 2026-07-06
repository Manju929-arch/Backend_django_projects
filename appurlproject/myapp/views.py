from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view1(request):
    a = a = "<h1 style='color:blue;'>Django class is started. Hello, welcome to Django class.</h1>"
    return HttpResponse(a)
