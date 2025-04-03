from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('تشكيل اللحية', 'تشكيل اللحية'),
        ('حلاقة رجالية', 'حلاقة رجالية'),
        ('خدمة شاملة من باربرشوب ليجند', 'خدمة شاملة من باربرشوب ليجند'),
        ('إزالة الشعر بالحلاوة', 'إزالة الشعر بالحلاوة'),
        ('استشارة الحلاقة الشخصية', 'استشارة الحلاقة الشخصية'),
        ('صبغ الشعر', 'صبغ الشعر'),
        ('تلوين الشعر/اللحية', 'تلوين الشعر/اللحية'),
        ('حلاقة الأطفال', 'حلاقة الأطفال'),
        ('حلاقة الرجال', 'حلاقة الرجال'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.service} - {self.date} {self.time}"
