from django.urls import path
from . import views
urlpatterns=[
    path('home/',views.home,name='home'),
    path('base/',views.base,name='base'),
    path('project/',views.project,name='project'),
    path('about/',views.about_view,name='about'),
    path('contact/',views.contact,name='contact'),
    path('certificate/',views.certificate_view,name='certificate')

]