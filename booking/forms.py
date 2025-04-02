from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking
from datetime import datetime, time as time_obj

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class BookingForm(forms.ModelForm):
    # توليد أوقات من 12:00 إلى 22:00
    TIME_CHOICES = [(f"{hour:02d}:00", f"{hour}:00") for hour in range(12, 23)]
    time = forms.ChoiceField(choices=TIME_CHOICES)

    class Meta:
        model = Booking
        fields = ['service', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',  # ✅ لتفعيل التقويم في المتصفح
                'class': 'form-control'
            }),
        'time': forms.Select(attrs={
            'class': 'form-control'
        }),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # إضافة class لجميع الحقول
        self.fields['service'].widget.attrs.update({'class': 'form-control'})
        self.fields['time'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time_str = cleaned_data.get('time')

        if date and time_str:
            # تحويل الوقت من نص إلى كائن وقت
            try:
                selected_time = datetime.strptime(time_str, "%H:%M").time()
            except ValueError:
                raise forms.ValidationError("الوقت غير صالح.")

            selected_datetime = datetime.combine(date, selected_time)
            now = datetime.now()

            # ✅ منع الحجز في الماضي
            if selected_datetime < now:
                raise forms.ValidationError("لا يمكنك الحجز في وقت مضى.")

            # ✅ منع الحجز بفارق أقل من ساعتين
            existing_bookings = Booking.objects.filter(date=date)
            for booking in existing_bookings:
                existing_time = datetime.combine(booking.date, booking.time)
                time_difference = abs((existing_time - selected_datetime).total_seconds()) / 3600
                if time_difference < 2:
                    raise forms.ValidationError("يوجد حجز آخر قريب من هذا الموعد. الرجاء اختيار وقت مختلف بفارق ساعتين.")
