from ..base import *

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "formatters": {
        "simple": {
            "format": "%(levelname)s %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple"
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "sentry": {
            "level": "ERROR",
            "class": "raven.contrib.django.handlers.SentryHandler",
        },
    },
    "root": {
        "handlers": ["console", "sentry"],
        "level": "INFO",
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "sentry.errors": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False,
        },
    }
}

SITE_ID = 3

JINJA_CONFIG.update({
    "auto_reload": False,
})

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

SERVER_EMAIL = "server@crate.io"
DEFAULT_FROM_EMAIL = "support@crate.io"
CONTACT_EMAIL = "support@crate.io"

PACKAGE_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"
PACKAGE_FILE_STORAGE_OPTIONS = {
    "bucket": "crate-production",
    "custom_domain": "packages.crate-cdn.com",
}

DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"
# STATICFILES_STORAGE = "storages.backends.s3boto.S3BotoStorage"

AWS_STORAGE_BUCKET_NAME = "crate-media-production"
AWS_S3_CUSTOM_DOMAIN = "media.crate-cdn.com"

AWS_STATS_BUCKET_NAME = "crate-logs"
AWS_STATS_LOG_REGEX = "^(cloudfront\.production/|cloudfront/production/packages/)"

INTERCOM_APP_ID = "79qt2qu3"

SIMPLE_API_URL = "https://simple.crate.io/"

# Security
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31556926
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
