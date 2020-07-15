"""
WSGI config for fido project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# from gevent import monkey
# from psycogreen.gevent import patch_psycopg

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")

# monkey.patch_all()
# patch_psycopg()

application = get_wsgi_application()
