from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('حلاقة كلاسيكية', 'حلاقة كلاسيكية'),
        ('تنظيف بشرة', 'تنظيف بشرة'),
        ('صبغة شعر', 'صبغة شعر'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.service} - {self.date} {self.time}"
