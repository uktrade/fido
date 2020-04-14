"""
Django settings for fido project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import os
import environ
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV_FILE = os.path.join(BASE_DIR, ".environ")

if os.path.exists(ENV_FILE):
    environ.Env.read_env(ENV_FILE)

env = environ.Env(DEBUG=(bool, False), RESTRICT_ADMIN=(bool, False))

DEBUG = env.bool("DEBUG", default=False)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# ALLOWED_HOSTS = [
# 'financeadmin-dev.cloudapps.digital',
# 'd3sy7fs6o4dizv.cloudfront.net',
# 'fido.uat.uktrade.io','fna.uat.uktrade.io']

# Application definition

INSTALLED_APPS = [
    "custom_usermodel",
    "authbroker_client",
    # 'admintool_support.apps.AdmintoolSupportConfig',
    "downloadsupport.apps.DownloadSupportConfig",
    "forecast.apps.ForecastConfig",
    # 'dit_user_management',
    "gifthospitality.apps.GifthospitalityConfig",
    "payroll.apps.PayrollConfig",
    "costcentre.apps.CostCentreConfig",
    "chartofaccountDIT.apps.ChartAccountConfig",
    "treasuryCOA.apps.TreasuryCOAConfig",
    "treasurySS.apps.TreasurySSConfig",
    "core.apps.CoreConfig",
    "end_of_month.apps.EndOfMonthConfig",
    "importdata.apps.ImportDataConfig",
    "upload_file.apps.UploadFileConfig",
    "download_file.apps.DownloadFileConfig",
    "pingdom.apps.PingdomConfig",
    "django_extensions",
    "django_tables2",
    "django_filters",
    "django_admin_listfilter_dropdown",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bootstrap4",
    "dal",
    "dal_select2",
    "bootstrap_datepicker_plus",  # https://pypi.org/project/django-bootstrap-datepicker-plus/  # noqa
    "storages",
    "sass_processor",
    "webpack_loader",
    "django_bootstrap_breadcrumbs",
    "guardian",
    "reversion",
    "rest_framework",
    "simple_history",
    "axes",
    "adv_cache_tag",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django_settings_export.settings_export",
            ]
        },
    }
]

WSGI_APPLICATION = "config.wsgi.application"

if 'VCAP_SERVICES' in os.environ:
    services = json.loads(os.getenv('VCAP_SERVICES'))
    DATABASE_URL = services['postgres'][0]['credentials']['uri']
else:
    DATABASE_URL = os.getenv('DATABASE_URL')

DATABASES = {
    "default": env.db()
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},  # noqa
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "en-gb"  # must be gb for date entry to work

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Remove extra details in the label
# for the filter fields, it does
# not says 'contains' or similar
def FILTERS_VERBOSE_LOOKUPS():
    from django_filters.conf import DEFAULTS

    verbose_lookups = DEFAULTS["VERBOSE_LOOKUPS"].copy()
    verbose_lookups.update({
            "icontains": "",
            "contains": "",
            "startswith": "",
            "istartswith": ""
        }
    )
    return verbose_lookups


AUTH_USER_MODEL = "custom_usermodel.User"

AUTHBROKER_URL = env("AUTHBROKER_URL", default=None)
AUTHBROKER_CLIENT_ID = env("AUTHBROKER_CLIENT_ID", default=None)
AUTHBROKER_CLIENT_SECRET = env("AUTHBROKER_CLIENT_SECRET", default=None)
AUTHBROKER_SCOPES = "read write"

LOGIN_URL = "/auth/login"
LOGIN_REDIRECT_URL = "index"
GIT_COMMIT = env("GIT_COMMIT", default=None)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

# Django webpack loader
WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "BUNDLE_DIR_NAME": "build/",  # must end with slash
        "STATS_FILE": os.path.join(BASE_DIR, "../front_end/config/webpack-stats.json"),
    }
}

# AWS
if 'VCAP_SERVICES' in os.environ:
    services = json.loads(os.getenv('VCAP_SERVICES'))
    credentials = services['aws-s3-bucket'][0]['credentials']

    AWS_ACCESS_KEY_ID = credentials["aws_access_key_id"]
    AWS_SECRET_ACCESS_KEY = credentials["aws_secret_access_key"]
    AWS_REGION = credentials["aws_region"]
    AWS_S3_REGION_NAME = credentials["aws_region"]
    AWS_STORAGE_BUCKET_NAME = credentials["bucket_name"]
else:
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID', default='')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY', default='')
    AWS_REGION = env('AWS_REGION', default='')
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME', default='')

AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

AWS_DEFAULT_ACL = None

# File storage
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# Redis
if 'VCAP_SERVICES' in os.environ:
    services = json.loads(os.getenv('VCAP_SERVICES'))
    credentials = services['redis'][0]['credentials']
    REDIS_URL = "rediss://:{}@{}:{}/0?ssl_cert_reqs=required".format(
        credentials['password'],
        credentials['host'],
        credentials['port'],
    )
else:
    REDIS_URL = env("CELERY_BROKER_URL", default=None)

# celery
CELERY_BROKER_URL = REDIS_URL
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"

CAN_ELEVATE_SSO_USER_PERMISSIONS = False
CAN_CREATE_TEST_USER = False

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "sass_processor.finders.CssFinder",
]

NUM_META_COLS = 8

CLAM_AV_USERNAME = env("CLAM_AV_USERNAME", default=None)
CLAM_AV_PASSWORD = env("CLAM_AV_PASSWORD", default=None)
CLAM_AV_URL = env("CLAM_AV_URL", default=None)
GTM_CODE = env("GTM_CODE", default=None)

SETTINGS_EXPORT = [
    'DEBUG',
    'GTM_CODE',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "core.no_cache_middleware.NoCacheMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
    "axes.middleware.AxesMiddleware",
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "guardian.backends.ObjectPermissionBackend",
    "axes.backends.AxesBackend",
]

AXES_LOGIN_FAILURE_LIMIT = 5

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# s3chunkuploader
FILE_UPLOAD_HANDLERS = ('s3chunkuploader.file_handler.S3FileUploadHandler',)
CLEAN_FILE_NAME = True

# Max and min for forecast entry values
MAX_FORECAST_FIGURE = 100000000
MIN_FORECAST_FIGURE = -100000000
