import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
AUTH_USER_MODEL = 'accounts_app.User'	# appName.Model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSRF_COOKIE_SECURE=False
# List of URLS you don't have to be loggin to view
LOGIN_EXEMPT_URLS = (
	r'^$',
	r'^about/$',
	r'^account/login/$',
	r'^account/register/$',
	r'^blog/$',
)
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/signup/'
MEDIA_URL = '/media/'	# Shown in browser
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')	# Internal hierarchy
ROOT_URLCONF = 'dashboard_app.urls'
#STATIC_ROOT= os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'	# Shown in browser
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static'),
]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v!9kjps6v-7@#&d7a6rz6v(815nxvo7kd&t$ihjf^_on0q^p5h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
	'dashboard_app',
	'accounts_app',
	'posts_app',
	'scholarship_map',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
    )
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware', 				# This is what appends forward slashes to URLS
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'dashboard_app.middleware.LoginRequriedMiddleware',	# Our custom middleware
]



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],	# 'HighlightPage_Project/templates/' to place in specific app
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

WSGI_APPLICATION = 'dashboard_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',			# The dbms you're using
		'NAME': 'loginsystem',							# The db itself
		'USER': 'root',									# Default from XAMPP Apache phpmyadmin.ini
		'PASSWORD': '',									# Default from XAMPP Apache phpmyadmin.ini
		'HOST': 'localhost',							# ...
		'PORT': '3306',										# Find one
		'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
	}
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
