from .settings import *

env_file = str(PROJECT_ROOT.path('security/environ_local.env'))
environ.Env.read_env(str(env_file))

DEBUG = env.bool('DEBUG')

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
SECRET_KEY = open(SECRET_FILE).read().strip()

# Database
DATABASES = {
    'default': env.db("SQLITE_URL"),
}

# CACHES = {
#     'default': env.cache('REDIS_URL')
# }

DJANGO_APPS = (

)
THIRD_PARTY_APPS = (
    'debug_toolbar',
    'django_extensions'
)
LOCAL_APPS = (

)
INSTALLED_APPS += DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
CONFIG_DEFAULTS = {
    'RESULTS_CACHE_SIZE': 3,
    'SHOW_COLLAPSED': True,
    'SQL_WARNING_THRESHOLD': 100,
}
INTERNAL_IPS = [
    # '127.0.0.1',
]
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
DEBUG_TOOLBAR_PATCH_SETTINGS = True

# https://www.google.com/settings/security/lesssecureapps
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND')
EMAIL_CONFIG = env.email_url('EMAIL_URL')
vars().update(EMAIL_CONFIG)

ADMIN_URL = env('ADMIN_URL')

# SESSION_COOKIE_SECURE = False
# SESSION_COOKIE_HTTPONLY = False
# CSRF_COOKIE_SECURE = False

LOGGING['loggers'].update({
    '{{ project_name|lower }}': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True,
    },
    'django': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True,
    },
    'django.db.backends': {
        'handlers': ['django'],
        'level': 'DEBUG',
        'propagate': False,
    },
    'performance': {
        'handlers': ['console'],
        'level': 'INFO',
        'propagate': True,
    },
})
