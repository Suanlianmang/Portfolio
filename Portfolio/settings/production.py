from .keys import *
import psycopg2
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': keys.DB_NAME,
        'USER': keys.DB_USER,
        'PASSWORD': keys.DB_PASSWORD,
        'HOST': 'localhost',
        'PORT': '',
    }
}