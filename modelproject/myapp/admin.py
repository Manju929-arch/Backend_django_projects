from django.contrib import admin
from myapp.models import student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','age','email','marks','dob']
admin.site.register(student,StudentAdmin)
