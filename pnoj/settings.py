"""
Django settings for pnoj project.

Generated by 'django-admin startproject' using Django 3.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import kubernetes as k8s

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '<secret key here>'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'judge',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_s3_storage',
    # 'django_registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'captcha',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pnoj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'pnoj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    # Override DATABASES
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'judge.User'

LOGIN_REDIRECT_URL = '/accounts/profile'

LOGOUT_REDIRECT_URL = "/"

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'emails'

SITE_ID = 1

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}


EMAIL_BACKEND = '<your email backend>'

# S3 STORAGE CONFIGURATION
# FOLLOW https://github.com/etianen/django-s3-storage
DEFAULT_FILE_STORAGE = ""
AWS_REGION = ''
AWS_S3_ENDPOINT_URL = ""
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_S3_BUCKET_NAME = ''
AWS_S3_FILE_OVERWRITE = False

STATICFILES_STORAGE = ""
AWS_S3_BUCKET_NAME_STATIC = ""
AWS_S3_BUCKET_AUTH_STATIC = False
AWS_S3_ENDPOINT_URL_STATIC = ""

# K8s CONFIGURATION
# FOLLOW https://github.com/kubernetes-client/python/blob/master/kubernetes/README.md

# ========================

languages = {
    'py3': {
        'code': 'py3',
        'name': 'Python3',
        'docker_image': 'pnoj/python3:v1.2'
        },
    'java8': {
        'code': 'java8',
        'name': 'Java 8',
        'docker_image': 'pnoj/java8:v1.2'
    },
    'c++17': {
        'code': 'c++17',
        'name': 'C++17',
        'docker_image': 'pnoj/cpp17:v1.2'
    },
}

cpu_limit = "800m"

tos_url = "https://wiki.oj.paullee.dev/Judge:Terms"

# ACCOUNT_ACTIVATION_DAYS = 7
# REGISTRATION_OPEN = True
# REGISTRATION_SALT = '<registration salt here>'

ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

RECAPTCHA_PUBLIC_KEY = '<your recaptcha public key>'
RECAPTCHA_PRIVATE_KEY = '<your recaptcha private key>'

ACCOUNT_FORMS = {'signup': 'judge.forms.PNOJSignupForm'}

try:
    from pnoj.config.config import *
except ImportError:
    print("Please create a config file to override values in settings.py")
