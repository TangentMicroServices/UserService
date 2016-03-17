from django.conf import settings

VERSION = "1"
SITE_ID=1

## docker settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
ALLOWED_HOSTS = ['.consul']
DEBUG = True

settings.INSTALLED_APPS.extend([
    # DRF:
    'rest_framework',
    'rest_framework_swagger',
    'rest_framework.authtoken',
	'corsheaders',

	# custom
	'api',
    'health',

    # testing etc:
    'django_jenkins',
    'django_extensions',    
])

USER_ROLES = [
    ('Director', 'Director'),
    ('Administrator', 'Administrator'),
    ('Developer', 'Developer'),
    ('Employee', 'Employee')]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ),
#    'DEFAULT_FILTER_BACKENDS': (
#        'rest_framework.filters.DjangoFilterBackend',
#        'rest_framework.filters.SearchFilter',
#        'rest_framework.filters.OrderingFilter',
#    ),
}

# Services:

## Service base urls without a trailing slash:
USERSERVICE_BASE_URL = 'http://userservice.staging.tangentmicroservices.com'
HOURSSERVICE_BASE_URL = 'http://hoursservice.staging.tangentmicroservices.com'

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
)

PROJECT_APPS = (
    'api',
)

CORS_ORIGIN_ALLOW_ALL = True
VERSION = 1


TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

#'--spec-color', '-s', # specify these on the command line (they'll mess with build server's tess)
NOSE_ARGS = ['--with-spec', 
             '--with-coverage', '--cover-html', '--cover-erase', '--with-xunit', '--cover-xml',
             '--cover-package=.', '--cover-html-dir=reports/cover']
