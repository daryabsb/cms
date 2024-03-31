from src.settings.components.env import config


# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=1)
SECRET_KEY = config("DJANGO_SECRET_KEY", default=None)


try:
    DEBUG = int(DEBUG)
except ValueError:
    if DEBUG == 'true':
        DEBUG = 1
    else:
        DEBUG = 0

ALLOWED_HOSTS = ['172.16.10.49', 'https://rebwarallaf.com']

ALLOWED_HOST = config("ALLOWED_HOST", cast=str, default="*")
if ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(ALLOWED_HOST.strip())