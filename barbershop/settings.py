from pathlib import Path
import os

# المسار الرئيسي
BASE_DIR = Path(__file__).resolve().parent.parent

# الأمان
SECRET_KEY = 'django-insecure-barbershop-v2'
DEBUG = False  # ← تم تعطيله لأنك تستخدم الاستضافة

ALLOWED_HOSTS = ['.onrender.com', '127.0.0.1', 'localhost']

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booking',
    # تسجيل الدخول عبر Google
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

SITE_ID = 1

# تسجيل الدخول عبر Google
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# الوسيطات
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # ✅ هذا موجود
    'allauth.account.middleware.AccountMiddleware',              # ✅ أضفه هنا
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'barbershop.urls'

# إعدادات القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # ← مهم لتفعيل request في القوالب
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'barbershop.wsgi.application'

# قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# تحقق كلمة المرور (للتطوير فقط)
AUTH_PASSWORD_VALIDATORS = []

# اللغة والمنطقة الزمنية
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# الملفات الثابتة (CSS/JS/Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'booking/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# إعادة التوجيه بعد تسجيل الدخول والخروج
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/login/'  # ✅ هذا السطر المهم لإصلاح الخطأ عند عدم تسجيل الدخول

# إعدادات البريد أثناء التطوير (تظهر في الطرفية فقط)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@barbershop.com'

# ✅ لتفادي التحذير الخاص بالمفتاح الافتراضي للـ models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
