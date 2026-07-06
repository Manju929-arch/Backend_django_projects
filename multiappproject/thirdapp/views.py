from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view3(request):
    a = "This is the response from the Third APP"
    return HttpResponse(a)