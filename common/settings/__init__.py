"""
Django settings
"""
import os

try:
    if os.environ['APP_ENV'] == 'local':
        from common.settings.local import *
    elif os.environ['APP_ENV'] == 'development':
        from common.settings.dvelopment import *
    elif os.environ['APP_ENV'] == 'staging':
        from common.settings.staging import *
    elif os.environ['APP_ENV'] == 'production':
        from common.settings.production import *
    else:
        from common.settings.local import *
except KeyError:
    from common.settings.local import *
finally:
    from common.settings.base import *
