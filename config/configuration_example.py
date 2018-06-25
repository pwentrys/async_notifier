from utils.strings import Strings as s
from .credentials import SQL_USER, SQL_PASS, SQL_SCHEMA
from .models.config import Config
from .models.sqlenvs import SQLEnvs
from .models.webenvs import WebEnvs

appname = s.appname
appnamelower = appname.lower()
is_debug = False  # SUPER IMPORTANT

config = Config({
    'name': appname,
    'cookie_domain': f'{appnamelower}',
    'cookie_name': f'{appnamelower}_dev' if is_debug else f'{appnamelower}',
    'debug': is_debug,
    'web': WebEnvs({
        'dev': {
            'name': f'Dev',
            'address': f'0.0.0.0',
            'port': 8020,
            'secret_key': f'SUPER_SECRET_DEV',
            'lifetime': 1  # session lifetime in days.
        },
        'prod': {
            'name': f'Prod',
            'address': f'0.0.0.0',
            'port': 5020,
            'secret_key': f'SUPER_SECRET',
            'lifetime': 1  # session lifetime in days.
        },
    }),
    'sql': SQLEnvs({
        'mysql': {
            'USERNAME': SQL_USER,
            'PASSWORD': SQL_PASS,
            'DATABASE': SQL_SCHEMA,
            'CONFIGS': '?charset=utf8',
            'ADDRESS': '0.0.0.0',
            'PORT': 3306,
        }
    })
})
