from .base import *  # noqa
import os


DEBUG = False
#TEMPLATES['OPTIONS']['debug'] = DEBUG

#SECRET_KEY = os.environ["SECRET_KEY"]

#ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')
ALLOWED_HOSTS = ['home.turbomansion.com']

ADMINS = (
    ('Uli', 'uli@turbomansion.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'turbosmarthome',
        'USER': 'turbosmarthome',
        'PASSWORD': 'WdhhrCAv%8cu',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
