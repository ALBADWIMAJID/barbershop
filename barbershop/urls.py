from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),
    path('accounts/', include('allauth.urls')),  # ✅ مهم لتسجيل الدخول باستخدام Google
]
