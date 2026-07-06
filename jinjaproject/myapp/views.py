from django.shortcuts import render

# Create your views here.
def view1(request):
    Name = "Rama"
    Place = "Bengaluru"
    ctx= {'Name': Name, 'Place':Place}
    return render(request,'my.html',ctx)
