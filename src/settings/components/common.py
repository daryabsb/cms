
from src.settings.components.env import config
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from src.settings.components import PROJECT_PATH, BASE_DIR


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

BASE_ENDPOINT = config('BASE_ENDPOINT', default='http://127.0.0.1:8000')
WS_ENDPOINT = config('WS_ENDPOINT', default='ws://127.0.0.1:8000')

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]
THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'django_extensions',
    'widget_tweaks',
    'mptt',
    'ckeditor',
    'ckeditor_uploader',
]
LOCAL_APPS = [
    'src.accounts',
    'src.core',
    # DASHBOARD APPS
    'src.dashboard',
    'src.dashboard.cms',

    'src.blogs',
    'src.comment',
    'src.contactus',
    'src.menu',
    'src.reels',
    'src.sliders',
    'src.subscribe',
    'src.pages',

    # Frontends
    'src.industico',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

AUTH_USER_MODEL = "accounts.User"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [

            PROJECT_PATH + 'templates',
            PROJECT_PATH + 'accounts' + 'templates',
            PROJECT_PATH + 'dashboard' + 'templates',
            PROJECT_PATH + 'pages' + 'templates',
            PROJECT_PATH + 'blogs' + 'templates',
            PROJECT_PATH + 'menu' + 'templates',

            PROJECT_PATH + 'reels' + 'templates',
            PROJECT_PATH + 'sliders' + 'templates',
            PROJECT_PATH + 'subscribe' + 'templates',
            PROJECT_PATH + 'contactus' + 'templates',

            # Frontend templates
            PROJECT_PATH + 'industico' + 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'custom_context_processor.dz_static',
                'custom_context_processor.site_config',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
