from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'date', 'time')
    list_filter = ('service', 'date')
    search_fields = ('user__username', 'service')
