from django.shortcuts import render
from myapp.models import student
# Create your views here.

def fakeview(resquest):
   s = student.objects.all()
   d = {'stud':s}
   return render( resquest, 'fake.html',d)
