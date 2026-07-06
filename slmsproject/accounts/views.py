from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from accounts.models import Profile
from django.http import HttpResponse
from django.contrib.auth import authenticate ,login
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request ,'home.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        user = User.objects.create_user(username = username, password = password)
        Profile.objects.create(user = user, role = role)
        return redirect('login')   
    return render(request , 'register.html')    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            if user.profile.role == 'admin':
                return redirect('admin_dashboard')
            else:
                return HttpResponse('staff_dashboard')
    return render(request, 'login.html')
    
@login_required
def admin_dashboard(request):
    if request.user.profile.role!='admin':
        return HttpResponse("staff_dashboard")
    return render(request ,'admin_dashboard.html')

@login_required
def delete_staff(request, id):

    profile = Profile.objects.filter(user=request.user).first()

    if not profile or profile.role != 'admin':
        return redirect('staff_dashboard')

    staff = User.objects.get(id=id)

    staff.delete()

    return redirect('manage_staff')