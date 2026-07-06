from django.contrib import admin
from myapp.models import product

# Register your models here.
class productadmin(admin.ModelAdmin):
    list_display=['p_name','p_manfacture','p_exp','p_mail']
admin.site.register(product,productadmin)
