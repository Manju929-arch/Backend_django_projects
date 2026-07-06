from django.shortcuts import render,redirect
from myapp.models import student
from myapp.form import studentForm

# Create your views here.
def display(request):
   s =  student.objects.all()
   d = {'stud':s}
   return render(render,'display.html', d)
def insert_view(request):
   f = studentForm()
   if request.method == "POST":
      f = studentForm(request.POST)
      if f.is_valid():
         f.save()
         return redirect('/')
   d = {'form':f}
   return render(request, 'form.html',d)

def update_view(request ,id):
   s = student.objects.get(id = id)
   f = studentForm(instance=s)
   if request.method == "POST":
      f= studentForm(request.POST, instance= s)
      if f.is_valid():
         f.save()
         return redirect('/')
   d = {'form':f}
   return render (request, 'form.html',d)

def delete_view(request, id):
   s = student.objects.get(id =id)
   s.delete()
   return redirect('/')
      

