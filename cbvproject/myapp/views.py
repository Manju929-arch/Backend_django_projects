from django.shortcuts import render
from django.views.generic import ListView ,DetailView,UpdateView,DeleteView,CreateView
from myapp.models import student
from django.urls import reverse_lazy
# Create your views here.
class studentList(ListView):
    model = student
    #default templates :student_list.html
    #default context : student_list

class studentdetails(DetailView):
    model = student
    #default templates :student_details.html
    #default context :student

class studentUpdate(UpdateView):
    model = student
    fields = "__all__"
    # defualt templates : student_form.html
    #default context: form

class studentDelete(DeleteView):
    model  = student
    success_url = reverse_lazy('student')
    #success_url is used to display the target page
    #default templates : student_confirm_delete.html
    #default context :student

class studentCreate(CreateView):
    model = student
    fields = '__all__'
    #default templates :student_from.html
    #default context :form
