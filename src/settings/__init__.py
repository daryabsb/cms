from split_settings.tools import include
from os import environ

ENV = environ.get('DJANGO_ENV') or 'local'

base_settings = [
    'components/paths.py',
    'components/secretes.py',
    'components/db.py',
    'components/common.py',
    'components/cors.py',
]

include(*base_settings)