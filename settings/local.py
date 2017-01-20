from .base import *  # noqa


ADMINS = (
    ('Uli', 'uli@turbomansion.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS=['neohaven.sorjak.com', '104.154.106.204']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'docker',
        'USER': 'docker',
        'HOST': 'postgres',
        'PASSWORD' : 'docker',
        'PORT': 5432,  # Set to empty string for default.
    }
}


# You might want to use sqlite3 for testing in local as it's much faster.
if IN_TESTING:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/tmp/turbosmarthome_test.db',
        }
    }


INSTALLED_APPS += ('django_extensions', )