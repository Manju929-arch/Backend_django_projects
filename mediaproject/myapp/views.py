from django.shortcuts import render
from myapp.models import product

# Create your views here.
def product_list(request):
    products = product.objects.all()
    ctx ={'prod':products}

    return render(request, 'product_list.html',ctx)
