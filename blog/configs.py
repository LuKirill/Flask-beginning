import os

from dotenv import load_dotenv

from blog.enums import EnvType



ENV = os.getenv('FLASK_ENV', default=EnvType.PRODUCTION)
DEBUG = ENV == EnvType.DEVELOPMENT

SECRET_KEY = os.getenv('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True

FLASK_ADMIN_SWATCH = 'pulse'


OPENAPI_URL_PREFIX = '/api/docs'
OPENAPI_VERSION = '3.0.0'
OPENAPI_SWAGGER_UI_PATH = '/'
OPENAPI_SWAGGER_UI_VERSION = '3.51.1'


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = ')c46i=c^-in+6v4^%cw$m11m5ubaz(3vob1ffcdysa5+t@+tdj'
    WTF_CSRF_ENABLED = True


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestingConfig(BaseConfig):
    TESTING = True


load_dotenv()