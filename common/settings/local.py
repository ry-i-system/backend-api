"""
Django local settings
"""
APP_ENV = 'local'
DEBUG = True

# 許可するオリジン
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080',
]