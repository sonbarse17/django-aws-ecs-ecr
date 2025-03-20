import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-j72u^@=mfq12mzz+&*p&7wm%v!&c7q9-*81@f!39u_x$j!8dd3'
# ...existing code...
INSTALLED_APPS = [
    # ...existing code...
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',  # This must be present
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "hello",
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Ensure this exists or adjust as needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Required for admin
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Required for admin
    'django.contrib.messages.middleware.MessageMiddleware',  # Required for admin
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ...existing code...
ROOT_URLCONF = "helloworld.urls"
# ...existing code...
ALLOWED_HOSTS = ["*"]
# ...existing code...
