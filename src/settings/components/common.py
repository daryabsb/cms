
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
    "django_htmx",
    'django.contrib.staticfiles',
    'django.contrib.humanize',

]
THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'django_extensions',
    'widget_tweaks',
    'mptt',
    'ckeditor',
    'ckeditor_uploader',
    "django_prose_editor",
    'after_response',
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

    # APIs
    'src._htmx',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

AUTH_USER_MODEL = "accounts.User"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "django_htmx.middleware.HtmxMiddleware",
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


CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"


CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',
        # 'skin': 'office2013',
        'pasteAsPlainText': True,
        'forcePasteAsPlainText': True,
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        # "removePlugins": "stylesheetparser",
        'toolbar_YourCustomToolbarConfig': [
            {
                'name': 'document', 
                'items': [
                'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': [
                'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': [
                'Find', 'Replace', '-', 'SelectAll']},
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
            {'name': 'styles', 'items': [
                'Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            # your extra plugins here
            'div',
            # 'section',
            # 'autolink',
            # 'autoembed',
            # 'embedsemantic',
            # 'autogrow',
            # 'devtools',
            # 'widget',
            # 'lineutils',
            # 'clipboard',
            # 'dialog',
            # 'dialogui',
            # 'elementspath',
            # 'a11yhelp',
            # 'about',
            # 'adobeair',
            # 'ajax',
            # 'bbcode',
            # 'codesnippet',
            # 'codesnippetgeshi',
            # 'colordialog',
            # 'devtools',
            # 'divarea',
            # 'docprops',
            # 'embed',
            # 'embedbase',
            # 'filetools',
            # 'find',
            # 'flash',
            # 'forms',
            # 'iframe',
            # 'iframedialog',
            # 'image',
            # 'image2',
            # 'language',
            # 'link',
            # 'liststyle',
            # 'magicline',
            # 'mathjax',
            # 'menubutton',
            # 'notification',
            # 'notificationaggregator',
            # 'pagebreak',
            # 'pastefromword',
            # 'placeholder',
            # 'preview',
            # 'scayt',
            # 'sharedspace',
            # 'showblocks',
            # 'smiley',
            # 'sourcedialog',
            # 'specialchar',
            # 'stylesheetparser',
            # 'table',
            # 'tableresize',
            # 'tabletools',
            # 'templates',
            # 'uicolor',
            # 'uploadwidget',
            # 'wsc',
            # 'xml'
        ]),
    }
}
