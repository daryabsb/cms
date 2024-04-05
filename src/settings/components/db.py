from src.settings.components.env import config
import dj_database_url
from src.settings.components import PROJECT_PATH, BASE_DIR

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR + 'db.sqlite3',
    }
}
