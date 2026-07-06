from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view2(request):
    a = "Welcome to  Django Second Class"
    return HttpResponse(a)
