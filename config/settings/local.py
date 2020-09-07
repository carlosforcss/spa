from config.settings.base import *

SECRET_KEY = '-m%z0q$46ii!)3ms7pzb59*kh=6$co7wsq^h%93r%qpnd&+^-w'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True
ALLOWED_HOSTS = ["*"]