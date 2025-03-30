from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('book/', views.make_booking, name='book'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('booking/edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),  # ✅ موجود فقط هنا
    path('booking/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
