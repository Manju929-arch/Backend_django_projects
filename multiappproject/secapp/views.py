from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view2(resquest):
    a = "This is the response from the Second APP"
    return HttpResponse(a)
