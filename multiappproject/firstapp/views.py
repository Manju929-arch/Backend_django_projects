from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view1(request):
   a = "<h1>this is the response from the firstapp"
   return HttpResponse(a)