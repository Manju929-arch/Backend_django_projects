from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'myapp/home.html')

def website(request):
    return render(request,'myapp/website.html')