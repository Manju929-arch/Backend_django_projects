from django.urls import path
from myapp2.views import view2
urlpatterns = [
    path('r2/',view2)
]