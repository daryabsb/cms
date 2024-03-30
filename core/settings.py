"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _


load_dotenv('.env')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '' #Put Your Email here

'''
Enable 2fa on your google account and create an apps password and use that in place of your true password in your code
'''

EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = '587'
EMAIL_USE_TLS = True

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =  True


ALLOWED_HOSTS = ['*']

SITE_ID=1

# Application definition


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'dashboard',
    'dashboard.users',
    'dashboard.cms.pages',
    'dashboard.cms.blog',
    'dashboard.cms.comment',
    'dashboard.cms.reels',
    'dashboard.cms.sliders',
    'dashboard.cms.menu',
    'dashboard.cms.subscribe',
    'dashboard.cms.contactus',
    'frontend',
    'mptt',
    'ckeditor', 
    'ckeditor_uploader',
    'rosetta',
    
    ]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                    BASE_DIR / 'frontend' / 'templates',
                    BASE_DIR / 'dashboard' / 'templates',
                    BASE_DIR / 'dashboard' / 'cms' / 'pages' / 'templates',
                    BASE_DIR / 'dashboard' / 'cms' / 'blog' / 'templates',
                    BASE_DIR / 'dashboard' / 'cms' / 'comment' / 'templates',
                    BASE_DIR / 'dashboard' / 'cms' / 'menu' / 'templates',
                    BASE_DIR / 'dashboard' / 'cms' / 'reels' / 'templates',
                    BASE_DIR / 'dashboard' / 'cms' / 'sliders' / 'templates',
                    BASE_DIR / 'dashboard' / 'cms' / 'subscribe' / 'templates',
                    BASE_DIR / 'dashboard' / 'cms' / 'contactus' / 'templates',
                    
                    ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'custom_context_processor.dz_static',
                'custom_context_processor.site_config',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'database' / 'theme5' / 'db.sqlite3',
    },
}



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'fop_db',
#         'USER': 'postgres',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/


LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', _('English')),
    ('hi', _('Hindi')),
    ('fr', _('French')),
    ('es', _('Spanish')),
)

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# The name of the cookie that stores the user's language preference
# LANGUAGE_COOKIE_NAME = 'dz_language_cookie'

# The name of the session key that stores the user's language preference
# LANGUAGE_SESSION_KEY = 'dz_language_session'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'


STATICFILES_DIRS = [
    BASE_DIR / 'dashboard' / 'static',
    BASE_DIR / 'frontend' / 'static',
    BASE_DIR / 'dashboard' / 'cms' / 'pages' / 'static',
    BASE_DIR / 'dashboard' / 'cms' / 'blog' / 'static',
    BASE_DIR / 'dashboard' / 'cms' / 'comment' / 'static',
    BASE_DIR / 'dashboard' / 'cms' / 'menu' / 'static',
    BASE_DIR / 'dashboard' / 'cms' / 'reels' / 'static',
    BASE_DIR / 'dashboard' / 'cms' / 'sliders' / 'static',
    BASE_DIR / 'dashboard' / 'cms' / 'subscribe' / 'static',
    BASE_DIR / 'dashboard' / 'cms' / 'contactus' / 'static',
]  

STATIC_ROOT = STATIC_ROOT = BASE_DIR / "static" 


MEDIA_URL = '/media/'
MEDIA_ROOT = Path(BASE_DIR, 'media')
CKEDITOR_UPLOAD_PATH = "uploads/"


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'

CKEDITOR_CONFIGS = {
    'default': {
        'removePlugins': 'stylesheetparser',
        'allowedContent': True,
        # 'extraAllowedContent': '*(*)',
        
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},

        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
      
        'height': 400,
        'width': '100%',
      
        'toolbarCanCollapse': True,
        'tabSpaces': 4,  
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
        ]),
    }
}


