from django.shortcuts import render
from myapp.models import product

# Create your views here.
def productview(request):
    p = product.objects.all()
    ctx = {'Product':p}
    return render(request,'pro.html,ctx')
