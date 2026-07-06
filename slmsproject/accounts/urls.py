from django.urls import path
from accounts import views
urlpatterns = [
    path('',views.home, name = 'home'),
    path('register/' ,views.register,name = 'register'),
    path('login/' ,views.login_view ,name = 'login'),
    path('admin_dashboard/',views.admin_dashboard,name = 'admin_dashboard'),
    path( 'delete_staff/<int:id>/', views.delete_staff,name='delete_staff'),
]
    
