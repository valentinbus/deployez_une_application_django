from . import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'disquaire',
        'USER': 'vbus',
        'PASSWORD': os.getenv('PASSWORD_DB'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
