from .settings import *

env_file = str(PROJECT_ROOT.path('security/environ_prod.env'))
environ.Env.read_env(str(env_file))

DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = ["*"]

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', RAW_TEMPLATE_LOADERS),
]

SECRET_KEY = SECRET_FILE

DATABASES = {
    'default': env.db("SQLITE_URL"),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['CONN_MAX_AGE'] = 10

CACHES = {
    'default': env.cache('REDIS_URL')
}

DJANGO_APPS = ()
THIRD_PARTY_APPS = (
    'storages',
)
LOCAL_APPS = (

)

INSTALLED_APPS += DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

ADMIN_URL = env('ADMIN_URL')

EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND')
EMAIL_URL = env.email_url('EMAIL_URL')
vars().update(EMAIL_URL)


# Caching sessions.
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = "default"

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

# --------------------AMAZON STORAGE----------------------------------
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_PRELOAD_METADATA = True

STATICFILES_LOCATION = 'static'
STATIC_URL = u"https://{0:s}/{1:s}/".format(AWS_S3_CUSTOM_DOMAIN,
                                            STATICFILES_LOCATION)
STATICFILES_STORAGE = 'project_name.apps.core.storage.storage_aws.StaticStorage'

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = u"https://{0:s}/{1:s}/".format(AWS_S3_CUSTOM_DOMAIN,
                                           MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'project_name.apps.core.storage.storage_aws.MediaStorage'


LOGGING['loggers'].update({
    '{{ project_name|lower }}': {
        'handlers': ['project'],
        'level': 'WARNING',
        'propagate': True,
    },
    'django': {
        'handlers': ['django'],
        'level': 'WARNING',
        'propagate': True,
    },
    'django.security.DisallowedHost': {
        'handlers': ['django'],
        'level': 'CRITICAL',
        'propagate': False,
    },
})
