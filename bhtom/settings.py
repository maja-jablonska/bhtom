"""
Django settings for your TOM project.

Originally generated by 'django-admin startproject' using Django 2.1.1.
Generated by ./manage.py tom_setup on Nov. 14, 2019, 11:18 p.m.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import tempfile

#reads all secret settings and apis, which will not be stored in git repo
try:
    from . import local_settings as secret
except ImportError:
    pass

#this is required by Heroku, as they setup environment variables instead of using local_settings (not on github)

try:
    LCO_APIKEY = secret.LCO_APIKEY
    SECRET_KEY = secret.SECRET_KEY
    ANTARES_KEY = secret.ANTARES_KEY
    ANTARES_SECRET = secret.ANTARES_SECRET
    TWITTER_APIKEY = secret.TWITTER_APIKEY
    TWITTER_SECRET = secret.TWITTER_SECRET
    TWITTER_ACCESSTOKEN = secret.TWITTER_ACCESSTOKEN
    TWITTER_ACCESSSECRET = secret.TWITTER_ACCESSSECRET
    TOMEMAIL = secret.TOMEMAIL
    TOMEMAILPASSWORD = secret.TOMEMAILPASSWORD
    SNEXBOT_APIKEY =  secret.TNSBOT_APIKEY
    black_tom_DB_USER = secret.black_tom_DB_USER 
    black_tom_DB_PASSWORD = secret.black_tom_DB_PASSWORD 
    CPCS_DATA_ACCESS_HASHTAG = secret.CPCS_DATA_ACCESS_HASHTAG
except:
    LCO_APIKEY = os.environ['LCO_APIKEY']
    SECRET_KEY = os.environ['SECRET_KEY']
    ANTARES_KEY = os.environ['ANTARES_KEY']
    ANTARES_SECRET = os.environ['ANTARES_SECRET']
    TWITTER_APIKEY = os.environ['TWITTER_APIKEY']
    TWITTER_SECRET = os.environ['TWITTER_SECRET']
    TWITTER_ACCESSTOKEN = os.environ['TWITTER_ACCESSTOKEN']
    TWITTER_ACCESSSECRET = os.environ['TWITTER_ACCESSSECRET']
    TOMEMAIL = os.environ['TOMEMAIL']
    TOMEMAILPASSWORD = os.environ['TOMEMAILPASSWORD']
    #tns harvester reads it too, but SNEXBOT api key still needed - FIX?
    SNEXBOT_APIKEY =  os.environ['TNSBOT_APIKEY']
    black_tom_DB_USER = os.environ['black_tom_DB_USER']
    black_tom_DB_PASSWORD = os.environ['black_tom_DB_PASSWORD']
    CPCS_DATA_ACCESS_HASHTAG = os.environ['CPCS_DATA_ACCESS_HASHTAG']

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u&amp;!)0%2f^l3n#g+#7ldg7xf)&amp;#eg79n+0gf0c@_v&amp;8wc9vp-3f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'guardian',
    'tom_common',
    'django_comments',
    'bootstrap4',
    'crispy_forms',
    'django_filters',
    'django_gravatar',
    'tom_targets',
    'tom_alerts',
    'tom_catalogs',
    'tom_observations',
    'tom_dataproducts',
    'myapp',
    'datatools',
]

SITE_ID = 0

MIDDLEWARE = [
#    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'tom_common.middleware.ExternalServiceMiddleware',
]

ROOT_URLCONF = 'myapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'myapp/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

WSGI_APPLICATION = 'bhtom.wsgi.application'
black_tom_DB_BACKEND = 'postgres'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
if black_tom_DB_BACKEND == 'postgres':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'bhtom',
            'USER': black_tom_DB_USER,
            'PASSWORD': black_tom_DB_PASSWORD,
            'HOST': 'localhost',
            'PORT': 5432,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATETIME_FORMAT = 'Y-m-d H:m:s'
DATE_FORMAT = 'Y-m-d'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# #STATIC_URL = '/static/'
# #LW: new from stackoverflow:
#STATIC_URL = os.path.join(BASE_DIR, 'static').replace('\\','')+'/'
STATIC_URL = '/Users/wyrzykow/bhtom/myapp/static/'

STATIC_ROOT = os.path.join(BASE_DIR, '_static')
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_DIRS  = ['/Users/wyrzykow/bhtom/myapp/static/']

MEDIA_ROOT = os.path.join(BASE_DIR, 'data')
MEDIA_URL = '/data/'

# STATIC_URL = '/static/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'data')
# MEDIA_URL = '/data/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    }
}

# Caching
# https://docs.djangoproject.com/en/dev/topics/cache/#filesystem-caching

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': tempfile.gettempdir()
    }
}

# TOM Specific configuration
TARGET_TYPE = 'SIDEREAL'

#LW: email server setup
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

FACILITIES = {
    'LCO': {
        'portal_url': 'https://observe.lco.global',
        'api_key':LCO_APIKEY,
    },
    'GEM': {
        'portal_url': {
            'GS': 'https://139.229.34.15:8443',
            'GN': 'https://128.171.88.221:8443',
        },
        'api_key': {
            'GS': '',
            'GN': '',
        },
        'user_email': '',
        'programs': {
            'GS-YYYYS-T-NNN': {
                'MM': 'Std: Some descriptive text',
                'NN': 'Rap: Some descriptive text'
            },
            'GN-YYYYS-T-NNN': {
                'QQ': 'Std: Some descriptive text',
                'PP': 'Rap: Some descriptive text',
            },
        },
    },
}

# Define the valid data product types for your TOM. Be careful when removing items, as previously valid types will no
# longer be valid, and may cause issues unless the offending records are modified.
DATA_PRODUCT_TYPES = {
    'photometry': ('photometry', 'Photometry'),
    'fits_file': ('fits_file', 'FITS File'),
    'spectroscopy': ('spectroscopy', 'Spectroscopy'),
    'image_file': ('image_file', 'Image File')
}

DATA_PROCESSORS = {
    'photometry': 'tom_dataproducts.processors.photometry_processor.PhotometryProcessor',
    'spectroscopy': 'tom_dataproducts.processors.spectroscopy_processor.SpectroscopyProcessor',
}

TOM_FACILITY_CLASSES = [
    'tom_observations.facilities.lco.LCOFacility',
    'tom_observations.facilities.gemini.GEMFacility'
]

TOM_ALERT_CLASSES = [
    'tom_alerts.brokers.mars.MARSBroker',
    'tom_alerts.brokers.lasair.LasairBroker',
    'tom_alerts.brokers.scout.ScoutBroker',
    'tom_alerts.brokers.tns.TNSBroker',
    'tom_antares.antares.AntaresBroker',
]

BROKER_CREDENTIALS = {
    'antares': {
        'api_key': ANTARES_KEY,
        'api_secret': ANTARES_SECRET
    }
}

# Define extra target fields here. Types can be any of "number", "string", "boolean" or "datetime"
# See https://tomtoolkit.github.io/docs/target_fields for documentation on this feature
# For example:
# EXTRA_FIELDS = [
#     {'name': 'redshift', 'type': 'number'},
#     {'name': 'discoverer', 'type': 'string'}
#     {'name': 'eligible', 'type': 'boolean'},
#     {'name': 'dicovery_date', 'type': 'datetime'}
# ]
EXTRA_FIELDS = [
    {'name': 'gaia_alert_name', 'type': 'string'},
    {'name': 'calib_server_name', 'type': 'string'},
    {'name': 'ztf_alert_name', 'type': 'string'},
    {'name': 'gaiadr2_id', 'type': 'string'},
    {'name': 'classification', 'type': 'string'},
    {'name': 'tweet', 'type': 'boolean'},
    {'name': 'jdlastobs', 'type': 'number'},
    {'name': 'maglast', 'type': 'number'},
    {'name': 'priority', 'type': 'number'},
    {'name': 'dicovery_date', 'type': 'datetime'},
    {'name': 'cadence', 'type': 'number'},
    {'name': 'Sun_separation', 'type': 'number'},
    {'name': 'dont_update_me', 'type':'boolean'}
]

# Authentication strategy can either be LOCKED (required login for all views)
# or READ_ONLY (read only access to views)
AUTH_STRATEGY = 'READ_ONLY'

# URLs that should be allowed access even with AUTH_STRATEGY = LOCKED
# for example: OPEN_URLS = ['/', '/about']
OPEN_URLS = []

HOOKS = {
#    'target_post_save': 'tom_common.hooks.target_post_save',
    'target_post_save': 'myapp.hooks.target_post_save',
    'observation_change_state': 'tom_common.hooks.observation_change_state',
    'data_product_post_upload': 'tom_dataproducts.hooks.data_product_post_upload',

}

#Gaia Alerts added by LW
#others are copied from default AbstractHarvester
TOM_HARVESTER_CLASSES = [
    'myapp.harvesters.gaia_alerts_harvester.GaiaAlertsHarvester',
    'tom_catalogs.harvesters.simbad.SimbadHarvester',
    'tom_catalogs.harvesters.ned.NEDHarvester',
    'tom_catalogs.harvesters.jplhorizons.JPLHorizonsHarvester',
    'tom_catalogs.harvesters.mpc.MPCHarvester',
    'tom_catalogs.harvesters.tns.TNSHarvester',
    ]

AUTO_THUMBNAILS = False

THUMBNAIL_MAX_SIZE = (0, 0)

THUMBNAIL_DEFAULT_SIZE = (200, 200)

HINTS_ENABLED = True
HINT_LEVEL = 20

try:
    from local_settings import * # noqa
except ImportError:
    pass
