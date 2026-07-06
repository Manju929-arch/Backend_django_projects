from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def Register(request):
    if request.method == "POST":
       username =  request.POST['username']
       password = request.POST['password']
       email = request.POST['email']
       User.objects.create_user(username = username, password = password ,email = email)
       return redirect("login")
    return render(request , 'register.html')
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username ,password = password)
        if user:
            login(request,user)
            return redirect('dashboard')
    return render(request, 'login.html')
@login_required
def dashboard(request):
    return render(request , 'dashboard.html')
@login_required
def logout_view(request):
    logout(request)
    return redirect('register')