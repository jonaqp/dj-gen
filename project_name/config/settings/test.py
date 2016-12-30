

from .settings import *

DEBUG = False
WSGI_APPLICATION = 'project_name.config.wsgi.test.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{{ project_name|lower }}',
        'USER': '{{ project_name|lower }}',
        'PASSWORD': '{{ project_name|lower }}',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'TEST': {
            'NAME': 'test_%s' % os.getenv('JOB_NAME', default='{{ project_name|lower }}')
        }
    }
}

INSTALLED_APPS += [
    'django_jenkins',
]

PROJECT_APPS = [app for app in INSTALLED_APPS if app.startswith('{{ project_name|lower }}')]

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.run_pep8',
)

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/stable/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

LOGGING['loggers'].update({
    'django': {
        'handlers': ['django'],
        'level': 'WARNING',
        'propagate': True,
    },
})
