"""
Django settings for dj_gen project.
"""
import environ
from django.utils.translation import ugettext_lazy as _

PROJECT_ROOT = environ.Path(__file__) - 3
print(PROJECT_ROOT)
APPS_DIR = PROJECT_ROOT.path('apps/')
print(APPS_DIR)
env = environ.Env()

SECRET_FILE = str(PROJECT_ROOT.path('security/SECRET.key'))
try:
    from django.utils.crypto import get_random_string

    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!$%&()=+-_'
    SECRET_KEY = get_random_string(50, chars)
    with open(SECRET_FILE, 'w') as f:
        f.write(SECRET_KEY)
        f.close()
except IOError:
    raise Exception('Could not open %s for writing!' % SECRET_FILE)

SECRET_KEY = 'zmji3zc+k_(&k+onhkl!if3z+dr)4bp-g_vye5v369532+prma'

DEBUG = True

ALLOWED_HOSTS = []

# Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'project_name.apps.core.apps.CoreConfig',
    'project_name.apps.user.apps.UserConfig',
)
THIRD_PARTY_APPS = (
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project_name.config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(PROJECT_ROOT.path('templates')),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project_name.config.wsgi.application'

# Password validation
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# Internationalization
LANGUAGES = [
    ('es', _('Spanish')),
    # ('en', _('English'))
]

LANGUAGE_CODE = 'en'

LOCALE_PATHS = (
    str(PROJECT_ROOT.path('locale')),
)

FIXTURE_DIR = (
    str(PROJECT_ROOT.path('fixture')),
)

SITE_ID = 1

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_ROOT = str(PROJECT_ROOT.path('run/static'))
MEDIA_ROOT = str(PROJECT_ROOT.path('run/media'))

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

AUTH_USER_MODEL = 'user.User'
LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = '/login/'
