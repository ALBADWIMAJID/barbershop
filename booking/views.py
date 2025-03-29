from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages

from .forms import SignUpForm, BookingForm
from .models import Booking


def home(request):
    return render(request, 'booking/home.html')


def services(request):
    return render(request, 'booking/services.html')


def about(request):
    return render(request, 'booking/about.html')


def contact(request):
    return render(request, 'booking/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'booking/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة.')
    return render(request, 'booking/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def dashboard(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/dashboard.html', {'bookings': bookings})


@login_required
def make_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()

            # إرسال بريد HTML احترافي
            subject = 'تأكيد الحجز - Barbershop'
            from_email = 'noreply@barbershop.com'
            to_email = [request.user.email]

            context = {
                'user': request.user,
                'booking': booking,
            }

            text_content = f"تم حجز خدمة: {booking.service} في {booking.date} الساعة {booking.time}"
            html_content = render_to_string('booking/email_confirmation.html', context)

            email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
            email.attach_alternative(html_content, "text/html")
            email.send()

            messages.success(request, 'تم الحجز بنجاح! تم إرسال تأكيد إلى بريدك الإلكتروني.')
            return redirect('dashboard')
    else:
        form = BookingForm()
    return render(request, 'booking/booking.html', {'form': form})
from django.shortcuts import get_object_or_404

@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تعديل الحجز بنجاح.')
            return redirect('dashboard')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking/booking.html', {'form': form, 'edit_mode': True})

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    messages.success(request, 'تم حذف الحجز بنجاح.')
    return redirect('dashboard')
