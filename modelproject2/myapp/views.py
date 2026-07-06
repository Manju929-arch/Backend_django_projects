from django.shortcuts import render
from myapp.models import student

# Create your views here.
def view1(resquest):
   s = student.objects.all()
   d = {'stud':s}
   return render( resquest, 'stud.html',d)
